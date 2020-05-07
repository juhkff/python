# 状态卡的简易表达形式
from nonebot import CommandSession, on_command
from nonebot.permission import EVERYBODY

from config import SUPERUSERS
from constant import super_help_content, help_content, super_help_content_c


@on_command('help', only_to_me=False, permission=EVERYBODY)
async def help_about(session: CommandSession):
    is_su = False
    qq = int(session.event.sender['user_id'])
    if qq in SUPERUSERS:
        is_su = True  # 是GM/KP
    if is_su:
        # GM/KP发起的查询
        await session.send(super_help_content)
    else:
        # PC发起的查询
        await session.send(help_content)


@on_command('helpc', only_to_me=False, permission=EVERYBODY)
async def help_about_pc(session: CommandSession):
    is_su = False
    qq = int(session.event.sender['user_id'])
    if qq in SUPERUSERS:
        is_su = True  # 是GM/KP
    if is_su:
        # GM/KP发起的查询
        await session.send(super_help_content_c)
        return
    else:
        # PC发起的查询
        return
