#!/usr/bin/python3

def no_c(my_string):
    for letter in my_string:
        if letter == 'c' or letter == 'C':
            my_string = my_string.translate({ord(letter): None})
    return my_string
