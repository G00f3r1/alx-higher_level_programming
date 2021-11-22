#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            row_len = len(row)
            i = 1
            for item in row:
                if row_len == i:
                    print("{:d}".format(item), end="")
                else:
                    print("{:d}".format(item), end=" ")
                i += 1
            print()
