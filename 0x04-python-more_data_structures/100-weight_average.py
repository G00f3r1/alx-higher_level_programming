#!/usr/bin/python3
def weight_average(my_list=[]):
    list_len = len(my_list)
    if list_len > 0:
        return sum([mul(x[0], x[1])for x in my_list])/sum(x[1]for x in my_list)
    else:
        return 0


def mul(x, y):
    return x * y
