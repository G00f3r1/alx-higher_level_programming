#!/usr/bin/python3

def uniq_add(my_list=[]):
    if my_list:
        result = 0
        my_list = set(my_list)
        for number in my_list:
            result += number
    return result
