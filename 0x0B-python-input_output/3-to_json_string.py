#!/usr/bin/python3
import json
"""
json is imported
"""


def to_json_string(my_obj):
    """
    fucntion to return representation of an object
    """
    data = json.dumps(my_obj)
    return data
