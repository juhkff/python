from nonebot import on_command
from nonebot.permission import GROUP_MEMBER, EVERYBODY, SUPERUSER

from constant import *
from plugins.alias.data_source import search_qq_alias
from plugins.health import is_number
from plugins.join.data_source import check_id, join_id, check_pc
from plugins.load.data_source import find_pc, read_pc, f_format, find_ps, read_ps, fs_format, fs_simple_format, read_pp, \
    fs_pp_format


@on_command('loadpc', only_to_me=False, permission=GROUP_MEMBER)
async def load_pc(session: CommandSession):
    try:
        test = str(session.event.sender['card'])
    except Exception:
        await session.send('此指令为群聊指令，仅在群聊有效！')
        return
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
    refresh_pc_card()


# su打印角色卡
@on_command('spc', only_to_me=False, permission=SUPERUSER)
async def s_load_pc(session: CommandSession):
    # 获得发送者的QQ号，检查是否在游戏中，不存在发送错误
    is_format = session.get('format')
    if not is_format:
        await session.send('./spc格式错误！./spc QQ')
        return
    # 格式正确
    change_qq = session.get('change_qq')
    sender_id = int(change_qq)  # 发送者的QQ号
    # sender_id = session.event.user_id  # 发送者的QQ号
    if check_id(sender_id) is not True:
        await session.send(sender_id + ' ' + id_not_found_info)
        return
    # 在游戏中则寻找状态卡，不存在发送错误
    if find_pc(sender_id) is not True:
        await session.send(sender_id + ' ' + id_pc_not_find)
        return
    # 存在角色卡
    player_state = read_pc(sender_id)
    result = str(sender_id) + 'の' + f_format(player_state)
    await session.send(result)
    refresh_pc_card()


# s_load_pc.args_parser装饰器将函数声明为s_load_pc命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@s_load_pc.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()
    arg = stripped_arg.split()  # split()函数默认可以按空格分割，并且把结果中的空字符串删除掉，留下有用信息
    if len(arg) != 1:
        session.state['format'] = False
        return
    elif not is_number(search_qq_alias(arg[0])):
        session.state['format'] = False
        return
    else:
        # arg长度位1
        qq = arg[0]
        qq = search_qq_alias(qq)
        # 格式正确
        session.state['format'] = True
        session.state['change_qq'] = qq


@on_command('loadps', only_to_me=False, permission=GROUP_MEMBER)
async def load_ps(session: CommandSession):
    try:
        test = str(session.event.sender['card'])
    except Exception:
        await session.send('此指令为群聊指令，仅在群聊有效！')
        return
    # 获得发送者的QQ号，检查是否在游戏中，不存在发送错误
    sender_id = session.event.user_id  # 发送者的QQ号
    if check_id(sender_id) is not True:
        await session.send(str(session.event.sender['card']) + ' ' + id_not_found_info)
        return
    # 在游戏中则寻找状态卡，不存在发送错误
    if find_ps(sender_id) is not True:
        await session.send(str(session.event.sender['card']) + ' ' + id_ps_not_find)
        return
    # 存在角色卡
    player_state = read_ps(sender_id)
    result = str(session.event.sender['card']) + 'の' + fs_format(player_state)
    await session.send(result)
    refresh_ps_card()


# su打印状态卡
@on_command('sps', only_to_me=False, permission=SUPERUSER)
async def s_load_ps(session: CommandSession):
    # 获得发送者的QQ号，检查是否在游戏中，不存在发送错误
    is_format = session.get('format')
    if not is_format:
        await session.send('./sps 格式错误！./sps QQ')
        return
    # 格式正确
    change_qq = session.get('change_qq')
    sender_id = int(change_qq)  # 发送者的QQ号
    # sender_id = session.event.user_id  # 发送者的QQ号
    if check_id(sender_id) is not True:
        await session.send(sender_id + ' ' + id_not_found_info)
        return
    # 在游戏中则寻找状态卡，不存在发送错误
    if find_ps(sender_id) is not True:
        await session.send(sender_id + ' ' + id_ps_not_find)
        return
    # 存在角色卡
    player_state = read_ps(sender_id)
    result = str(sender_id) + 'の' + fs_format(player_state)
    await session.send(result)
    refresh_ps_card()


# s_load_ps.args_parser装饰器将函数声明为s_load_ps命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@s_load_ps.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()
    arg = stripped_arg.split()  # split()函数默认可以按空格分割，并且把结果中的空字符串删除掉，留下有用信息
    if len(arg) != 1:
        session.state['format'] = False
        return
    elif not is_number(search_qq_alias(arg[0])):
        session.state['format'] = False
        return
    else:
        # arg长度位1
        qq = arg[0]
        qq = search_qq_alias(qq)
        # 格式正确
        session.state['format'] = True
        session.state['change_qq'] = qq


# 状态卡的简易表达形式
@on_command('state', only_to_me=False, permission=GROUP_MEMBER)
async def load_ps_simple(session: CommandSession):
    try:
        test = str(session.event.sender['card'])
    except Exception:
        await session.send('此指令为群聊指令，仅在群聊有效！')
        return
    # 获得发送者的QQ号，检查是否在游戏中，不存在发送错误
    sender_id = session.event.user_id  # 发送者的QQ号
    if check_id(sender_id) is not True:
        await session.send(str(session.event.sender['card']) + ' ' + id_not_found_info)
        return
    # 在游戏中则寻找状态卡，不存在发送错误
    if find_ps(sender_id) is not True:
        await session.send(str(session.event.sender['card']) + ' ' + id_ps_not_find)
        return
    # 存在角色卡
    player_state = read_ps(sender_id)
    player_card = str(session.event.sender['card'])  # 玩家群名称
    result = fs_simple_format(player_card, player_state)
    await session.send(result)
    refresh_ps_card()


# 状态卡的简易表达形式-GM/KP版
@on_command('sst', only_to_me=False, permission=SUPERUSER)
async def s_load_ps_simple(session: CommandSession):
    # 获得发送者的QQ号，检查是否在游戏中，不存在发送错误
    is_format = session.get('format')
    if not is_format:
        await session.send('./sst 格式错误！./sst QQ')
        return
    # 格式正确
    change_qq = session.get('change_qq')
    sender_id = int(change_qq)  # 发送者的QQ号

    if check_id(sender_id) is not True:
        await session.send(sender_id + ' ' + id_not_found_info)
        return
    # 在游戏中则寻找状态卡，不存在发送错误
    if find_ps(sender_id) is not True:
        await session.send(sender_id + ' ' + id_ps_not_find)
        return
    # 存在角色卡
    player_state = read_ps(sender_id)
    player_card = str(sender_id)  # 玩家群名称(划去)
    result = fs_simple_format(player_card, player_state)
    await session.send(result)
    refresh_ps_card()


# s_load_ps_simple.args_parser装饰器将函数声明为s_load_ps_simple命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@s_load_ps_simple.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()
    arg = stripped_arg.split()  # split()函数默认可以按空格分割，并且把结果中的空字符串删除掉，留下有用信息
    if len(arg) != 1:
        session.state['format'] = False
        return
    elif not is_number(search_qq_alias(arg[0])):
        session.state['format'] = False
        return
    else:
        # arg长度位1
        qq = arg[0]
        qq = search_qq_alias(qq)
        # 格式正确
        session.state['format'] = True
        session.state['change_qq'] = qq


# 属性卡的简易表达形式-GM/KP版
@on_command('spp', only_to_me=False, permission=SUPERUSER)
async def s_load_pp(session: CommandSession):
    # 获得发送者的QQ号，检查是否在游戏中，不存在发送错误
    is_format = session.get('format')
    if not is_format:
        await session.send('./spp 格式错误！./spp QQ')
        return
    # 格式正确
    change_qq = session.get('change_qq')
    sender_id = int(change_qq)  # 发送者的QQ号

    if check_id(sender_id) is not True:
        await session.send(sender_id + ' ' + id_not_found_info)
        return
    # 在游戏中则寻找状态卡，不存在发送错误
    if find_pc(sender_id) is not True:
        await session.send(sender_id + ' ' + id_pc_not_find)
        return
    # 存在角色卡
    player_pp = read_pp(sender_id)
    player_card = str(sender_id)  # 玩家群名称(划去)
    result = fs_pp_format(player_card, player_pp)
    await session.send(result)
    refresh_ps_card()


# s_load_ps_simple.args_parser装饰器将函数声明为s_load_ps_simple命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@s_load_pp.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()
    arg = stripped_arg.split()  # split()函数默认可以按空格分割，并且把结果中的空字符串删除掉，留下有用信息
    if len(arg) != 1:
        session.state['format'] = False
        return
    elif not is_number(search_qq_alias(arg[0])):
        session.state['format'] = False
        return
    else:
        # arg长度位1
        qq = arg[0]
        qq = search_qq_alias(qq)
        # 格式正确
        session.state['format'] = True
        session.state['change_qq'] = qq
