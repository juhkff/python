import configparser

from nonebot import CommandSession, on_command
from nonebot.permission import SUPERUSER

from constant import path_alias, new_alias_have, alias_not_have, alias_succeed, alias_fail
from plugins.alias.data_source import load_alias_as_string, load_alias_as_dict, alias_add, alias_del


@on_command('alias', only_to_me=False, permission=SUPERUSER)
async def alias(session: CommandSession):
    a_type = session.get('type')
    result = False
    if a_type == 'error':
        await session.send('/alias 格式错误！')
        return
    elif a_type == 'list':
        # 读取alias配置文件内容
        alias_content = load_alias_as_string()
        await session.send('[List]\n' + alias_content)
        return
    elif a_type == 'add':
        # 添加
        alias_dict = load_alias_as_dict()
        new_alias = session.get('alias')
        new_fact = session.get('fact')
        if new_alias in alias_dict:
            await session.send(new_alias_have)
            return
        # 可添加
        result = alias_add(new_alias, new_fact)
    elif a_type == 'del':
        # 删除
        alias_dict = load_alias_as_dict()
        del_alias = session.get('alias')
        if del_alias not in alias_dict:
            await session.send(alias_not_have)
            return
        # 可删除
        result = alias_del(del_alias)
    if result:
        await session.send(alias_succeed)
    else:
        await session.send(alias_fail)
    return


# alias.args_parser装饰器将函数声明为alias命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@alias.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()
    args = stripped_arg.split()  # split()函数默认可以按空格分割，并且把结果中的空字符串删除掉，留下有用信息
    if len(args) == 0:
        # 列表
        session.state['type'] = 'list'
        return
    if len(args) == 3 and args[0] == 'add':
        # 添加
        session.state['type'] = 'add'
        session.state['alias'] = args[1]
        session.state['fact'] = args[2]
        return
    if len(args) == 2 and args[0] == 'del':
        # 删除
        session.state['type'] = 'del'
        session.state['alias'] = args[1]
        return
    session.state['type'] = 'error'
    return
