#!/usr/bin/python3


def square_matrix_simple(matrix=[]):

    new_matrix = list(map(lambda numbers: list(map(lambda number: (number**2), numbers)), matrix ))
    return new_matrix
