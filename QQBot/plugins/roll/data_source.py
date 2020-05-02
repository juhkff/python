import random
import re


def match_roll(roll_str):
    pattern = re.compile(r'\d+d\d+')
    result = re.fullmatch(pattern, roll_str)
    if result is None:
        return False
    else:
        return True


# 投一次range范围的骰子
def roll_once(roll_range=int):
    number = random.randint(1, roll_range)
    return number


# 投掷times次，返回[总和,每次结果]
def roll_times(times, roll_range=int):
    result_list = [0] * times
    result = 0
    for i in range(0, times):
        one_result = roll_once(roll_range)
        result_list[i] = one_result
        result += one_result
    return [result, result_list]
