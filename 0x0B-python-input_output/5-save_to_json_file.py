#!/usr/bin/python3
""" json import """

import json


def save_to_json_file(my_obj, filename):
    """
    save to json file
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
