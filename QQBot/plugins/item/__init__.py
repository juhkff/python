from nonebot import on_command, CommandSession, get_bot
from nonebot.permission import SUPERUSER

from constant import id_pc_not_find, buff_add_have, buff_remove_not_have, buff_update_succeed, state_file_used, \
    item_add_have, item_remove_not_have, item_update_succeed
from plugins.alias.data_source import search_qq_alias
from plugins.buff.data_source import find_ps, update_buff
from plugins.health import is_number
from plugins.item.data_source import find_pc, update_item


@on_command('item', only_to_me=False, permission=SUPERUSER)
async def item(session: CommandSession):
    is_format = session.get('format')
    if not is_format:
        await session.send('/item 格式错误！./item QQ ± 物品名')
        return
    # 格式正确
    change_qq = int(session.get('change_qq'))
    op_type = session.get('op_type')
    item_name = session.get('item_name')
    # 在游戏中则寻找状态卡，不存在发送错误
    if find_pc(change_qq) is not True:
        await session.send(str(session.event.sender['card']) + ' ' + id_pc_not_find)
        return
    # 存在状态卡
    try:
        result_str = update_item(change_qq, op_type, item_name)
    except Exception:
        await session.send(state_file_used)
        return
    card = None
    try:
        bot = get_bot()
        member_list = await bot.get_group_member_list(group_id=session.event['group_id'])
        for member in member_list:
            if str(member['user_id']) == str(change_qq):
                card = member['card']
    except Exception:
        card = str(change_qq)

    if result_str == 'Have':
        await session.send('[' + card + ']' + item_add_have)
    if result_str == 'Not have':
        await session.send('[' + card + ']' + item_remove_not_have)
    if result_str == 'Succeed':
        await session.send('[' + card + ']' + item_update_succeed)
    return


# item.args_parser装饰器将函数声明为buff命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@item.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()
    args = stripped_arg.split()  # split()函数默认可以按空格分割，并且把结果中的空字符串删除掉，留下有用信息
    if len(args) != 3:
        session.state['format'] = False
        return
    else:
        # args长度位3
        item_name = args[2]
        op_type = args[1]
        qq = args[0]
        qq = search_qq_alias(qq)
        if not is_number(qq):
            # 不是数字
            session.state['format'] = False
            return
        if op_type != '+' and op_type != '-':
            # 不是操作符
            session.state['format'] = False
            return
        # buff_name的操作暂略
        # pass
        session.state['format'] = True
        session.state['change_qq'] = qq
        session.state['op_type'] = op_type
        session.state['item_name'] = item_name
        return
