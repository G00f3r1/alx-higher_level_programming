#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list:
        list_len = len(my_list)
        i = 0
        new_list = []
        while(list_len > i):
            if my_list[i] == search:
                new_list.append(replace)
            else:
                new_list.append(my_list[i])
            i += 1
    return new_list
