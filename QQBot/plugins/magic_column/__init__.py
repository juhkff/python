import nonebot
from nonebot import on_command, get_bot
from nonebot.permission import GROUP_MEMBER, SUPERUSER

from constant import *
from plugins.alias.data_source import search_qq_alias
from plugins.health.data_source import is_number, find_ps, change_hp
from plugins.join.data_source import check_id, join_id, check_pc
from plugins.magic_column.data_source import change_magic_column
from plugins.max_health.data_source import change_max_hp


@on_command('smagic', only_to_me=False, permission=SUPERUSER)
async def magic_column(session: CommandSession):
    is_format = session.get('format')
    if not is_format:
        await session.send('/smagic 格式错误！')
        return
    # 格式正确
    change_qq = session.get('change_qq')
    change_column = session.get('change_column')
    change_number = session.get('change_number')
    # 在游戏中则寻找状态卡，不存在发送错误
    if find_ps(change_qq) is not True:
        await session.send(str(session.event.sender['card']) + ' ' + id_pc_not_find)
        return
    # 存在状态卡，修改血量，得到最后的字符串
    cur_magic_column = 0
    nothing = False
    try:
        [cur_magic_column, nothing] = change_magic_column(change_qq, change_column, change_number)
    except Exception:
        await session.send(state_file_used)

    bot = get_bot()
    member_list = await bot.get_group_member_list(group_id=session.event['group_id'])
    card = None
    for member in member_list:
        if str(member['user_id']) == change_qq:
            card = member['card']
    if nothing:
        # 无可用法术位
        await session.send('[' + card + ']' + magic_column_nothing)
        return
    await session.send('[' + card + ']' + '剩余' + str(cur_magic_column) + '个' + change_column + '级法术位')
    return


# magic_column.args_parser装饰器将函数声明为magic_column命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@magic_column.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()
    args = stripped_arg.split()  # split()函数默认可以按空格分割，并且把结果中的空字符串删除掉，留下有用信息
    if len(args) != 3:
        session.state['format'] = False
        return
    else:
        # args长度位3
        number = args[2]
        column = args[1]
        qq = args[0]
        qq = search_qq_alias(qq)
        if not is_number(number):
            # 不是数字
            session.state['format'] = False
            return
        if not is_number(column):
            # 不是数字
            session.state['format'] = False
            return
        if int(column) > 9 or int(column) < 1:
            # 最多9个法术位1-9
            session.state['format'] = False
            return
        elif not is_number(qq):
            # 不是qq
            session.state['format'] = False
            return
        # 格式正确
        session.state['format'] = True
        session.state['change_qq'] = qq
        session.state['change_column'] = column
        session.state['change_number'] = number
        return
