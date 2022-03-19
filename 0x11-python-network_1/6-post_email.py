#!/usr/bin/python3

from sys import argv
import requests

if __name__ == "__main__":
    email = {'email': argv[2]}
    resp = requests.post(argv[1], email)
    print(resp.text)
