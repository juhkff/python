import nonebot
from nonebot import on_command, get_bot
from nonebot.permission import GROUP_MEMBER, SUPERUSER

from constant import *
from plugins.health.data_source import is_number, find_ps, change_hp
from plugins.join.data_source import check_id, join_id, check_pc


@on_command('health', only_to_me=False, permission=SUPERUSER)
async def health(session: CommandSession):
    is_format = session.get('format')
    if not is_format:
        await session.send('/hpchange 格式错误！')
        return
    # 格式正确
    change_qq = session.get('change_qq')
    change_number = session.get('change_number')
    # 在游戏中则寻找状态卡，不存在发送错误
    if find_ps(change_qq) is not True:
        await session.send(str(session.event.sender['card']) + ' ' + id_pc_not_find)
        return
    # 存在状态卡，修改血量，得到最后的字符串
    try:
        cur_hp = change_hp(change_qq, change_number)
    except Exception:
        await session.send(state_file_used)
        return
    bot = get_bot()
    member_list = await bot.get_group_member_list(group_id=session.event['group_id'])
    card = None
    for member in member_list:
        if str(member['user_id']) == change_qq:
            card = member['card']
    await session.send('[' + card + ']' + ' 目前血量为： ' + cur_hp)
    return


# health.args_parser装饰器将函数声明为hp命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@health.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()
    args = stripped_arg.split()  # split()函数默认可以按空格分割，并且把结果中的空字符串删除掉，留下有用信息
    if len(args) != 2:
        session.state['format'] = False
        return
    else:
        # args长度位2
        number = args[1]
        qq = args[0]
        if not is_number(number):
            # 不是数字
            session.state['format'] = False
            return
        elif not is_number(qq):
            # 不是qq
            session.state['format'] = False
            return
        # 格式正确
        session.state['format'] = True
        session.state['change_qq'] = qq
        session.state['change_number'] = number
        return
