import prettytable as pt
import re
from plugins.health.data_source import is_number

if __name__ == '__main__':  # 3d5
    pattern = re.compile(r'\d+d\d+')
    test = '5d6a'
    result = re.fullmatch(pattern, test)
    print(result is None)
