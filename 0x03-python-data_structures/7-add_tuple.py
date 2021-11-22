#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    tuple_a_len = len(tuple_a)
    tuple_b_len = len(tuple_b)

    if tuple_a_len < 2:
        if tuple_a_len == 1:
            new_tuple = (tuple_a[0] + tuple_b[0], 0 + tuple_b[1])
        else:
            new_tuple = (0 + tuple_b[0], 0 + tuple_b[1])
    elif tuple_b_len < 2:
        if tuple_b_len == 1:
            new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + 0)
        else:
            new_tuple = (tuple_a[0] + 0, tuple_a[1] + 0)
    else:
        new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_tuple
