#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response
"""

from sys import argv
from urllib import request, parse


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = parse.urlencode({"email": email})
    data = data.encode("ascii")
    with request.urlopen(url, data) as resp:
        print(resp.read().decode('utf-8'))
