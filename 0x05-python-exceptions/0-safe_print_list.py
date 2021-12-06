#!/usr/bin/python3
def list_len(my_list):
    len = 0
    for i in my_list:
        len += 1
    return len


def safe_print_list(my_list=[], x=0):
    index = 0
    try:
        for item in my_list:
            if index < x:
                print("{:d}".format(my_list[index]), end="")
                index += 1
        print()
        return index
    except IndexError:
        for item in my_list:
            print("{:d}".format(item), end="")
        return list_len(my_list)
