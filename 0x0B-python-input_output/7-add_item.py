#!/usr/bin/python3
"""
Nothing imported
"""


import sys
from os import path
from importlib.machinery import SourceFileLoader

# Importing modules using importlib
save_to_json_file = SourceFileLoader(
        "5-save_to_json_file", "5-save_to_json_file.py"
        ).load_module().save_to_json_file
load_from_json_file = SourceFileLoader(
        "6-load_from_json_file", "6-load_from_json_file.py"
        ).load_module().load_from_json_file

if not path.exists('add_item.json'):
    save_to_json_file([], 'add_item.json')

my_list = load_from_json_file('add_item.json')

my_list.extend(sys.argv[1:])

save_to_json_file(my_list, 'add_item.json')
