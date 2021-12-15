#!/usr/bin/python3


def text_indentation(text):
    """This is a function that prints a text with 2 new lines
       after each of these characters: ., ? and :
        Args:
            text (str): the text to be printed
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = ""
    string = text[:]
    for delm in ".?:":
        new_text = string.split(delm)
        string = ""
        for i in new_text:
            i = i.strip(" ")
            if string == "":
                string = i + delm
            else:
                string = string + "\n\n" + i + delm
    print(string)
