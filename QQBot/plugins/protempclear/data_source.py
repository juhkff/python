import configparser
import os

from docx import Document

from constant import path_settings, path_storage, origin_line


# 在ini文件中寻找名称
def search_name_in_settings(name):
    con = configparser.ConfigParser()
    con.read(path_settings, encoding='gbk')
    items = con.items('playerProp2')  # 返回元组
    a_dict = dict(items)
    items_real = con.items('playerProp')
    b_dict = dict(items_real)
    # name_list = list(a_dict.values())
    for index in a_dict:
        if a_dict[index] == name:
            return [True, index, str(b_dict[index])]  # 返回True以及该名称对应的key以及实际名字
    for index2 in b_dict:
        if b_dict[index2] == name:
            return [True, index2, name]
    return [False, None, None]


def temp_change_pro(sender_id, pro_name, pro_index):
    pro_index = int(pro_index)

    path = os.path.join(path_storage, str(sender_id))  # storage/qq/
    des_file = str(sender_id) + '_C.docx'
    path = os.path.join(path, des_file)  # storage/qq/qq_C.docx
    document = Document(path)
    tables = document.tables  # 获取文件中的表格集
    table = tables[0]

    index = 1
    between_index = 0
    between = [4, 3, 4, 1]
    # origin_line = 4
    for i in range(1, pro_index):
        index += between[between_index]
        between_index = (between_index + 1) % 4
    table_cell = table.cell(origin_line + int((index - 1) / 12), ((index - 1) % 12) + 1)
    origin_content = table_cell.text

    # origin_content = 原框中的内容
    if '(' not in str(origin_content):
        # 没有括号，先加上括号
        origin_content += '(0)'
    if '(' in str(origin_content):
        # 有括号的话
        split_list = str(origin_content).split('(')
        origin_number = int(split_list[0])
        origin_extra = str(split_list[1]).split(')')[0]  # '+5/0'
        origin_extra_number = int(origin_extra)
        difference = 0 - origin_extra_number
        result_number = str(origin_number + difference)
        # (左边处理完毕，结果为str变量result_number
        # 开始处理(右边,初始有str变量origin_extra，可能值有0/+5/-3
        result_extra_option = ''
        # result_extra_content = ''
        if origin_extra == '0':  # 初始为0
            result_extra = 0 + difference
            if result_extra > 0:
                result_extra_option = '+'
            result_extra_content = result_extra_option + str(result_extra)
        else:
            # '+5/-3'
            option = origin_extra[0]  # '+/-'
            number = int(origin_extra[1:])  # 5
            if option == '+':  # 初始为+5
                result_extra = number + difference  # 6/-1/0
                if result_extra > 0:
                    # 添加+
                    result_extra_option = '+'
                result_extra_content = result_extra_option + str(result_extra)
            else:  # 初始为-3
                result_extra = 0 - number + difference
                if result_extra > 0:
                    # 添加+
                    result_extra_option = '+'
                result_extra_content = result_extra_option + str(result_extra)
        # result_extra_content 即为结果str
        result_content = result_number + '(' + result_extra_content + ')'

        table_cell.text = str(result_content)
        document.save(path)
        final_content = table.cell(origin_line + int((index - 1) / 12), ((index - 1) % 12) + 1).text
        return final_content
