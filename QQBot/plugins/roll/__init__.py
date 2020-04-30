import random

import nonebot
from nonebot import on_command, CommandSession
from nonebot.permission import GROUP_MEMBER


@on_command('roll', only_to_me=False, permission=GROUP_MEMBER)
async def roll(session: CommandSession):
    number = random.randint(1, 100)
    await session.send(str(number))
