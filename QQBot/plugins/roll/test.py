import prettytable as pt

if __name__ == '__main__':
    tb = pt.PrettyTable()
    tb.field_names = ['1环', '2环', '3环', '4环', '5环', '6环', '7环', '8环', '9环']
    tb.add_row(['4', '3', '0', '0', '0', '0', '0', '0', '0'])

    result = str(tb)
    print(result)
