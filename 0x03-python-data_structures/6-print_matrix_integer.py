#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_len = len(row)
        for item in row:
            if row_len > 1:
                print("{:d}".format(item), end=" ")
            else:
                print("{:d}".format(item), end="")
        print()
