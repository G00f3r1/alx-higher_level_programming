#!/usr/bin/python3

from sys import argv
from urllib import request

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as resp:
            data = resp.read()
            print(data.decode("UTF-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
