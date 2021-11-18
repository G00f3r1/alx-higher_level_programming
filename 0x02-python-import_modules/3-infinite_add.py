#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_len = len(sys.argv) - 1
    sum = 0
    i = 1
    while(arg_len >= i):
        sum += int(sys.argv[i])
        i += 1
    print(sum)
