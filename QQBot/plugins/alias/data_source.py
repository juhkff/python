import configparser

from constant import path_settings


def load_alias_as_string():
    con = configparser.ConfigParser()
    con.read(path_settings, encoding='gbk')
    items = con.items('alias')  # 返回元组
    a_dict = dict(items)
    result = ''
    for each_key in a_dict:
        result += each_key + '=' + a_dict[each_key] + '\n'
    if result[-1] == '\n':
        result = result[:-1]
    return result


def load_alias_as_dict():
    con = configparser.ConfigParser()
    con.read(path_settings, encoding='gbk')
    items = con.items('alias')  # 返回元组
    a_dict = dict(items)
    return a_dict


def alias_add(new_alias, new_fact):
    con = configparser.ConfigParser()
    con.read(path_settings, encoding='gbk')
    con.set('alias', new_alias, new_fact)
    con.write(open(path_settings, 'r+'))
    alias_list = con.options('alias')
    if new_alias in alias_list:
        return True
    else:
        return False


def alias_del(del_alias):
    con = configparser.ConfigParser()
    con.read(path_settings, encoding='gbk')
    con.remove_option('alias', del_alias)
    con.write(open(path_settings, 'w'))
    alias_list = con.options('alias')
    if del_alias not in alias_list:
        return True
    else:
        return False


def search_qq_alias(qq_alias):
    con = configparser.ConfigParser()
    con.read(path_settings, encoding='gbk')
    alias_dict = load_alias_as_dict()
    if qq_alias in alias_dict:
        return alias_dict[qq_alias]
    else:
        return qq_alias
