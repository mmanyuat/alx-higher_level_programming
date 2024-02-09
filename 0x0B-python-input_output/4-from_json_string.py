#!/usr/bin/python3
"""
Module for json deserialization
"""

import json


def from_json_string(my_str):
    """
    function that returns python object
    """

    data = json.loads(my_str)
    return data
