from nonebot import on_command
from nonebot.permission import GROUP_MEMBER

from config import SUPERUSERS
from constant import *
from plugins.join.data_source import check_id, join_id, check_pc


@on_command('join', only_to_me=False, permission=GROUP_MEMBER)
async def join(session: CommandSession):
    is_su = False
    qq = int(session.event.sender['user_id'])
    if qq in SUPERUSERS:
        is_su = True  # 是GM/KP
    if is_su:
        await session.send(su_cannot_join)

    # 获得发送者的QQ号，检查是否在游戏中，已存在发送错误，不存在则添加到playerList.json中
    sender_id = session.event.user_id  # 发送者的QQ号
    if check_id(sender_id) is True:
        await session.send(str(session.event.sender['card']) + ' ' + id_found_info)
        return
    # 没找到则再寻找是否存在角色卡
    if check_pc(sender_id) is not True:
        await session.send(str(session.event.sender['card']) + ' ' + id_pc_not_found)
        return
    # 找到角色卡则将其加入
    result = join_id(sender_id)
    if result:
        await session.send(str(session.event.sender['card']) + ' ' + id_join_succeed)
        return
    await session.send('[加入游戏]' + ' ' + error_info)
