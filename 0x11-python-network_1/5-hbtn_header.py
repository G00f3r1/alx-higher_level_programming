#!/usr/bin/python3

from sys import argv
import requests

if __name__ == "__main__":
    resp = requests.get(argv[1])
    X_id = resp.headers.get("X-Request-Id")
    print(X_id)
