import math
import os

from docx import Document

from constant import path_storage, talent, origin_line, item_row


def find_pc(sender_id=int):
    path = os.path.join(path_storage, str(sender_id))  # storage/qq/
    file_list = os.listdir(path)
    des_file = str(sender_id) + '_C.docx'
    if des_file not in file_list:
        return False
    else:
        return True


def search_str(origin_list, search):
    if isinstance(origin_list, list):
        return search in origin_list


def update_item(sender_id=int, op_type=str, item_name=str):
    path = os.path.join(path_storage, str(sender_id))  # storage/qq/
    des_file = str(sender_id) + '_C.docx'
    path = os.path.join(path, des_file)  # storage/qq/qq_S.docx
    document = Document(path)
    tables = document.tables  # 获取文件中的表格集
    table = tables[0]

    item_content = table.cell(item_row, 0).text
    if len(item_content) > 0 and item_content[0] == ' ':
        item_content = item_content[1:]
    if len(item_content) > 0 and item_content[-1] == ' ':
        item_content = item_content[:-1]
    item_list = str(item_content).split()
    result_item = ''

    if op_type == '+':  # 允许重名
        # 加入新buff
        # if search_str(item_list, item_name):
        #    # 已经有该buff
        #    return 'Have'
        # else:
        for each in item_list:
            result_item += each + ' '
        result_item += str(item_name)
    elif op_type == '-':
        # 去除已有item
        done = False
        if not search_str(item_list, item_name):
            # 没有该item
            return 'Not have'
        else:
            for each in item_list:
                if each != item_name or done:
                    result_item += each + ' '
                else:
                    done = True
    if len(result_item) > 0 and result_item[0] == ' ':
        result_item = result_item[1:]
    if len(result_item) > 0 and result_item[-1] == ' ':
        result_item = result_item[:-1]
    # 将修改后的字符串内容重新写入
    table.cell(item_row, 0).text = result_item
    document.save(path)
    return 'Succeed'
