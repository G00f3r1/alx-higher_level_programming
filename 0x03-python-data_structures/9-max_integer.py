#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max_num = 0
        for item in my_list:
            if max_num < item:
                max_num = item
    return max_num
