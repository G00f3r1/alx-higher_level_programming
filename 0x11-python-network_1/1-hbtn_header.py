#!/usr/bin/python3

from sys import argv
from urllib import request

if __name__ == "__main__":
    with request.urlopen(argv[1]) as resp:
        data = resp.getheader("X-Request-Id")
        print(data)
