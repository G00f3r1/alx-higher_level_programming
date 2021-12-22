#!/usr/bin/python3
"""Defining script that adds all arguments to
a Python list, and then save them to a file."""
import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if os.path.exists("add_item.json"):
    arg_list = load_from_json_file('add_item.json')
else:
    arg_list = list()
    
n = len(sys.argv)

for i in range(1, n):
    arg_list.append(sys.argv[i])
save_to_json_file(arg_list, "add_item.json")
