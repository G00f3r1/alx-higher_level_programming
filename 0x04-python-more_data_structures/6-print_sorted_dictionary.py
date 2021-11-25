#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):

    sorted_dict = sorted(a_dictionary.items())

    for key, value in sorted(a_dictionary.items()):
        print("{} : {}".format(key, value))
