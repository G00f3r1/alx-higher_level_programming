#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    list_len = len(my_list)
    new_list = []
    i = 0
    while(list_len > i):
        if my_list[i] % 2 == 0:
            new_list.insert(i, True)
        else:
            new_list.insert(i, False)
        i += 1
    return new_list
