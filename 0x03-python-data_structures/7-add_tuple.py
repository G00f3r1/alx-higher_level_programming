#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) < 1:
        default = (0, 0)
        new_tuple = tuple(map(lambda i, j: i + j, tuple_a, default))
    elif len(tuple_b) < 2:
        default = (tuple_b[0], 0)
        new_tuple = tuple(map(lambda i, j: i + j, tuple_a, default))
    else:
        new_tuple = tuple(map(lambda i, j: i + j, tuple_a, tuple_b))
    return new_tuple
