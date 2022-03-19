#!/usr/bin/python3
"""
script that takes repository name and owner name
arguments and list 10 commits
"""

from sys import argv
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits"
    resp = requests.get(url.format(argv[2], argv[1]))
    commits = resp.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
