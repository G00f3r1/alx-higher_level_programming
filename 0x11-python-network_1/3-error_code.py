#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
and displays the body of the response
"""

from sys import argv
from urllib import request


if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as resp:
            data = resp.read()
            print(data.decode("UTF-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
