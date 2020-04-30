import os

from nonebot import CommandSession

project_root = os.path.dirname(os.path.realpath(__file__))
path_storage = os.path.join(project_root, 'storage')
path_playerList = os.path.join(path_storage, 'playerList.json')
path_playerProp = os.path.join(path_storage, 'playerProp.json')

max_items = 8

# const_row = '---------------------------------------------------------------------------------'
const_row = '-----------------------'
id_found_info = '已在游戏中，不可重复加入'
id_not_found_info = '未加入游戏'
id_pc_found = '已有角色卡，不可重复创建'
id_pc_not_find = '角色卡未找到'
id_pc_not_found = '角色卡未创建，不可加入'
id_ps_not_find = '状态卡未找到'
id_ps_not_found = '状态卡未创建，不可见如'
id_join_succeed = '加入成功'

error_info = '处理出错...'

# 该项修改时，此变量下面的方法和相关代码段也要随之修改
talent = {
    '天赋1': None,
    '天赋2': None,
    '天赋3': None,
    '天赋4': None,
    '天赋5': None,
    '天赋6': None,
    '天赋7': None,
    '天赋8': None
}


def refresh_pc_card(global_talent):
    # 部分职业没有这两个选项所以要清除
    pc_card['法术'] = None
    pc_card['法术上限'] = None

    global_talent['天赋1'] = None
    global_talent['天赋2'] = None
    global_talent['天赋3'] = None
    global_talent['天赋4'] = None
    global_talent['天赋5'] = None
    global_talent['天赋6'] = None
    global_talent['天赋7'] = None
    global_talent['天赋8'] = None


items = [None] * max_items

# 角色卡
pc_card = {
    '姓名': None,
    '性别': None,
    '年龄': None,
    '种族': None,
    '职业': None,
    '天赋': talent,
    '精通': None,
    '职业等级': None,
    '熟练加值': None,
    '戏法': None,
    '法术': None,
    '戏法上限': None,
    '法术上限': None,
    '人物介绍': None
}

# 同理，改动的同时也要改动下面和相关代码段
ps_card = {
    '血量': None,
    '血量上限': None,
    '经验值': None,
    '经验值上限': None,
    '每环法术位': [None] * 9,
    'Buff': None,
    'Debuff': None
}


def refresh_ps_card():
    ps_card['每环法术位'] = [None] * 9
    ps_card['Buff'] = None
    ps_card['Debuff'] = None


for i in range(max_items):
    pc_card['物品'] = items
# def check_private(session: CommandSession):
#     message_type = session.event.sub_type
#     if message_type != 'group':
#         return False
#     return True
