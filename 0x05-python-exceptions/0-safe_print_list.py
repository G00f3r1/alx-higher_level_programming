#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    index = 0
    l_len = 0
    try:
        for item in my_list:
            if index < x:
                print("{:d}".format(my_list[index]), end="")
                index += 1
            l_len += 1
        print()
        return index
    except IndexError:
        for item in my_list:
            print("{:d}".format(item), end="")
        return l_len
