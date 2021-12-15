#!/usr/bin/python3


def text_indentation(text):
    """This is a function that prints a text with 2 new lines
       after each of these characters: ., ? and :
        Args:
            text (str): the text to be printed
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        if char == "." or char == "?" or char == ":":
            print(char, end="\n\n")
        else:
            print(char, end="")
