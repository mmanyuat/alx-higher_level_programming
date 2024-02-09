#!/usr/bin/python3
"""
Module is to provide a function for json serialation
"""

import json


def to_json_string(my_obj):
    """
    fucntion to return representation of an object
    """
    data = json.dumps(my_obj)
    return data
