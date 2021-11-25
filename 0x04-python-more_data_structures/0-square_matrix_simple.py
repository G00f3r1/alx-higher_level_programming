#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    matrix_len = len(matrix)
    new_matrix = []

    if matrix_len > 0:
        for number in matrix[:]:
            new_matrix.append(list(map(lambda x: x ** 2, number)))
    return new_matrix
