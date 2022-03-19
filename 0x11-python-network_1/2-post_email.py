#!/usr/bin/python3

from sys import argv
from urllib import request, parse

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = parse.urlencode({"email": email})
    data = data.encode("ascii")
    with request.urlopen(url, data) as resp:
        print(resp.read().decode('utf-8'))
