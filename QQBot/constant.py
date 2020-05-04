import configparser
import os

from nonebot import CommandSession

project_root = os.path.dirname(os.path.realpath(__file__))
path_settings = os.path.join(project_root, 'gamesettings.ini')
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
magic_column_nothing = '剩余法术位不足，操作失败'
state_file_used = '[Failed:To GM]修改状态时文档不能处于打开状态！'
buff_add_have = '已有此buff！'
buff_remove_not_have = '本来就没有此buff！'
debuff_add_have = '已有此debuff！'
debuff_remove_not_have = '本来就没有此debuff！'
buff_update_succeed = 'buff更改成功'
debuff_update_succeed = 'debuff更改成功'
new_alias_have = '已有该别名！'
alias_not_have = '没有该别名！'
su_cannot_join = 'GM/KP不可加入游戏！'
alias_succeed = '操作成功！'
alias_fail = '命名失败...'
error_info = '处理出错...'

# 帮助文本
help_content = \
    'PC指令列表：\n' \
    '[/join]---加入游戏\n' \
    '[/roll 2d5]---投掷5面骰子2次\n' \
    '[/loadpc]---打印角色卡\n' \
    '[/loadps]---打印状态卡\n' \
    '[/state]---简易打印状态卡\n' \
    '[/game]---查看游戏方法'

# GM/KP帮助文本
super_help_content = \
    'GM/KP指令列表：\n' \
    '[/roll 2d5]---投掷5面骰子2次\n' \
    '[/sbuff QQ ± buff名]---对应PC±buff\n' \
    '[/sdebuff QQ ± debuff名]---对应PC±debuff\n' \
    '[/shealth QQ ±5]---对应PC血量±5\n' \
    '[/smaxhealth QQ ±5]---对应PC血量上限±5\n' \
    '[/smagic QQ 1~9 ±2]--对应PC法术位1~9栏数量±2\n' \
    '[/sloadpc QQ]---打印角色卡\n' \
    '[/sloadps QQ]---打印状态卡\n' \
    '[/sstate QQ]---简易打印状态卡\n' \
    '[/alias]---查看别名列表\n' \
    '[/alias add 别名 QQ]---增加别名代替较难输的QQ\n' \
    '[/alias del 别名]---删除别名'

game_step = \
    '[如何使用机器人进行跑团]\n' \
    '将指定格式的角色卡和状态卡发给我\n' \
    '确定文件导入后使用[/join]指令加入游戏\n' \
    '游戏即可\n' \
    '（暂时没有做退出游戏的方法）\n' \
    'GM/PC的指定需要我手动操作'

con = configparser.ConfigParser()
con.read(path_settings, encoding='gbk')
pp_list = con.items('playerProp')  # 返回元组
pp_dict = dict(pp_list)
pp_num = len(pp_dict)  # 属性数量
talent = {}  # 创建字典
for talent_index in pp_dict:
    talent[pp_dict[talent_index]] = None


# 该项修改时，此变量下面的方法和相关代码段也要随之修改
# talent = {
#     '力量': None,
#     '敏捷': None,
#     '智力': None,
#     '体质': None,
#     '感知': None,
#     '魅力': None,
#     '护甲等级': None,
#     '属性8': None
# }


def refresh_pc_card():
    # 部分职业没有这两个选项所以要清除
    pc_card['法术'] = None
    pc_card['法术上限'] = None

    for index in pp_dict:
        talent[pp_dict[index]] = None


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
