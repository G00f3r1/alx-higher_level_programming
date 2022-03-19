#!/usr/bin/python3

from sys import argv
import requests

if __name__ == "__main__":
    url = "https://api.github.com/user"
    resp = requests.get(url, auth=(argv[1], argv[2])).json()
    print(resp.get("id"))
