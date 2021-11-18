#!/usr/bin/python3
import sys

arg_len = len(sys.argv) - 1

if (arg_len == 0):
    print("{:d} arguments.".format(arg_len))
elif (arg_len == 1):
    print("{:d} argument:".format(arg_len))
else:
    print("{:d} arguments:".format(arg_len))

i = 1
while(arg_len >= i):
    print("{:d}: {}".format(i, sys.argv[i]))
    i += 1
