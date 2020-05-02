from nonebot import CommandSession, on_command
from nonebot.permission import EVERYBODY

from config import SUPERUSERS
from constant import super_help_content, help_content, game_step


@on_command('game', only_to_me=False, permission=EVERYBODY)
async def help_game(session: CommandSession):
    await session.send(game_step)
