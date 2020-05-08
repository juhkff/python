from nonebot import on_command, get_bot
from nonebot.permission import SUPERUSER

from constant import *
from plugins.alias.data_source import search_qq_alias
from plugins.health.data_source import is_number
from plugins.load import find_pc

from plugins.protemp.data_source import search_name_in_settings
from plugins.protempclear.data_source import temp_change_pro


@on_command('tpc', only_to_me=False, permission=SUPERUSER)
async def temp_pro_clear(session: CommandSession):
    is_format = session.get('format')
    if not is_format:
        await session.send('./tpc 格式错误！./tpc QQ 已有属性名')
        return
    # 格式正确
    change_qq = session.get('change_qq')
    pro_name = session.get('pro_name')
    pro_index = session.get('pro_index')
    # 在游戏中则寻找角色卡，不存在发送错误
    if find_pc(change_qq) is not True:
        await session.send(str(session.event.sender['card']) + ' ' + id_pc_not_find)
        return
    # 存在角色卡，修改属性值，得到最后的字符串
    try:
        cur_pro_content = temp_change_pro(change_qq, pro_name, pro_index)
    except Exception:
        await session.send(state_file_used)
        return
    try:
        bot = get_bot()
        member_list = await bot.get_group_member_list(group_id=session.event['group_id'])
        card = None
        for member in member_list:
            if str(member['user_id']) == change_qq:
                card = member['card']
    except Exception:
        card = change_qq
    await session.send('[' + card + ']' + ' 目前' + pro_name + '为： ' + cur_pro_content)
    return


# pro_change.args_parser装饰器将函数声明为hp命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@temp_pro_clear.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()
    args = stripped_arg.split()  # split()函数默认可以按空格分割，并且把结果中的空字符串删除掉，留下有用信息
    if len(args) != 2:
        session.state['format'] = False
        return
    else:
        # args长度位2
        pro_name = args[1]
        qq = args[0]
        qq = search_qq_alias(qq)
        if not is_number(qq):
            # 不是qq
            session.state['format'] = False
            return
        else:
            [result, index, name] = search_name_in_settings(pro_name)
            if not result:
                # 属性名错误
                session.state['format'] = False
                return
                # 格式正确
        session.state['format'] = True
        session.state['change_qq'] = qq
        session.state['pro_name'] = name
        session.state['pro_index'] = index
        return
