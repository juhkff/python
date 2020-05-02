import random

import nonebot
from nonebot import on_command, CommandSession
from nonebot.permission import GROUP_MEMBER, EVERYBODY

from plugins.roll.data_source import match_roll, roll_times


@on_command('roll', only_to_me=False, permission=EVERYBODY)
async def roll(session: CommandSession):
    is_format = session.get('format')
    if not is_format:
        await session.send('/roll 格式错误！/roll 次数d范围')
        return
    # 格式正确
    times = int(session.get('times'))
    row_range = int(session.get('range'))
    [result, result_list] = roll_times(times, row_range)
    result_str = '投掷结果：'
    if times > 1:
        # 大于1次投掷
        for each_number in result_list:
            result_str += str(each_number) + '+'
        result_str = result_str[:-1]
        result_str += ' = '
        result_str += str(result)
    else:
        # 只投掷1次
        result_str += ' ' + str(result) + ' / ' + str(row_range)
    await session.send(result_str)


# roll.args_parser装饰器将函数声明为magic_column命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@roll.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    arg = session.current_arg_text.strip()
    if not match_roll(arg):
        # 格式不对
        session.state['format'] = False
        return
    else:
        session.state['format'] = True
        arg_list = arg.split('d')
        times = arg_list[0]  # 投掷次数
        row_range = arg_list[1]  # 每次投掷骰子的大小范围
        session.state['times'] = times
        session.state['range'] = row_range
        return
