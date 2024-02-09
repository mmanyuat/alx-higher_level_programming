#!/usr/bin/python3
"""
json file
"""
import json


def load_from_json_file(filename):
    """
    Load from json file to python object
    """

    with open(filename, 'r') as file:
        obj = json.load(file)
        return obj
