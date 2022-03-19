#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id
in the response header
"""

from sys import argv
import requests


if __name__ == "__main__":
    resp = requests.get(argv[1])
    X_id = resp.headers.get("X-Request-Id")
    print(X_id)
