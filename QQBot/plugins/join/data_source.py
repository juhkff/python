import json

from constant import *


# 检查QQ号是否已经在playerList.json中
def check_id(qq):
    file = open(path_playerList, 'r', encoding='UTF-8')
    player_list = json.load(file)
    if isinstance(player_list, list):
        if qq in player_list:
            return True
    return False


# 将QQ号加入playerList.json中
def join_id(qq):
    file = open(path_playerList, 'r+', encoding='UTF-8')
    player_list = json.load(file)
    if isinstance(player_list, list):
        player_list.append(qq)
        file.seek(0)
        file.truncate()  # 清空文件
        json.dump(player_list, file)
        return True


# 根据QQ号寻找是否存在角色卡    路径：storage/qq/qq.docx
def check_pc(qq):
    file_list = os.listdir(path_storage)
    des_name = str(qq)
    final_name = des_name + '_C.docx'
    final_name_s = des_name + '_S.docx'
    if des_name in file_list:
        file = os.listdir(os.path.join(path_storage, des_name))
        if final_name not in file:
            # 不存在角色卡
            return False
        elif final_name_s not in file:
            # 不存在状态卡
            return False
        else:
            return True
    return False
