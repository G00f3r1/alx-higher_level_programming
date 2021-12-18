#!/usr/bin/python3
"""Defining matrix_divided function"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix.
    Args:
        matrix(list): must be a list of lists of integers or floats
        div(int): must be a number (integer or float)
    raise:
        TypeError: if matrix is not a list of intigers or floats and
            if matrix is not the same size, and if div is not intiger
            or float
        ZeroDivisionError: if div is 0.
    return: new list contening the result of the division
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    items_sizes = set()    
    new_list = []
    for items in matrix:
        if check_for_list(items) is False:
            raises_type_error()
            
        items_sizes = check_size_inconsistency(items_sizes, items)
        new = []
        for item in items:
            if check_for_number(item) is False:
                raises_type_error()
            new.append(round(item / div, 2))
        new_list.append(new)
    return new_list

"""Checks if matrix is (list of lists) of integers/floats"""
def check_for_list(new):
    
    if type(new) is not list or len(new) == 0:
        raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')

"""Checks if a number is int or float"""
def check_for_number(new):
    
    if type(new) is not int and type(new) is not float:
        return False
    if new != new:
        return False

    return True

"""Check if size of a list is equal"""
def check_size_inconsistency(items_sizes, row):

    items_sizes.add(len(row))

    if len(items_sizes) > 1:
        raise TypeError('Each row of the matrix must have the same size')

    return items_sizes

"""rasin exception TypeError"""
def raises_type_error():
    
    raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
