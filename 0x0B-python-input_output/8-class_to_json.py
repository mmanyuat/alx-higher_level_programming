#!/usr/bin/python3
""" Nothing """


def class_to_json(obj):
    """ Returns the dictionary description for JSON serialization"""
    json_dict = {}
    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value
    return json_dict
