from nonebot import on_command
from nonebot.permission import GROUP_MEMBER, EVERYBODY

from constant import *
from plugins.join.data_source import check_id, join_id, check_pc
from plugins.loadPC.data_source import find_pc, read_pc, f_format, find_ps, read_ps, fs_format


@on_command('loadpc', only_to_me=False, permission=EVERYBODY)
async def load_pc(session: CommandSession):
    # 获得发送者的QQ号，检查是否在游戏中，不存在发送错误
    sender_id = session.event.user_id  # 发送者的QQ号
    if check_id(sender_id) is not True:
        await session.send(str(session.event.sender['card']) + ' ' + id_not_found_info)
        return
    # 在游戏中则寻找角色卡，不存在发送错误
    if find_pc(sender_id) is not True:
        await session.send(str(session.event.sender['card']) + ' ' + id_pc_not_find)
        return
    # 存在角色卡
    player_card = read_pc(sender_id)
    result = str(session.event.sender['card']) + 'の' + f_format(player_card)
    await session.send(result)
    refresh_pc_card(talent)


@on_command('loadps', only_to_me=False, permission=EVERYBODY)
async def load_ps(session: CommandSession):
    # 获得发送者的QQ号，检查是否在游戏中，不存在发送错误
    sender_id = session.event.user_id  # 发送者的QQ号
    if check_id(sender_id) is not True:
        await session.send(str(session.event.sender['card']) + ' ' + id_not_found_info)
        return
    # 在游戏中则寻找状态卡，不存在发送错误
    if find_ps(sender_id) is not True:
        await session.send(str(session.event.sender['card']) + ' ' + id_pc_not_find)
        return
    # 存在角色卡
    player_state = read_ps(sender_id)
    result = str(session.event.sender['card']) + 'の' + fs_format(player_state)
    await session.send(result)
    refresh_ps_card()
