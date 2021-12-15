#!/usr/bin/python3
"""This module Defines print_square"""


def text_indentation(text):
    """This is a function that prints a text with 2 new lines
       after each of these characters: ., ? and :
        Args:
            text (str): the text to be printed
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    count = 0
    while count < len(text) and text[count] == ' ':
        count += 1

    while count < len(text):
        print(text[count], end="")
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count += 1
            while count < len(text) and text[count] == ' ':
                count += 1
            continue
        count += 1
