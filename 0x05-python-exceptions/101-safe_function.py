#!/usr/bin/python
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except ZeroDivisionError as zde:
        sys.stderr.write("Exception: " + str(zde) + "\n")
        return None
    except IndexError as ie:
        sys.stderr.write("Exception: " + str(ie) + "\n")
        return None
