#!/usr/bin/python
"""a basic serialization module"""
import json


def serialize_and_save_to_file(data, filename):
    """
    serialize a Python dictionary to a JSON file and
    deserialize the JSON file to recreate the Python Dictionary
    """
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """load and deserialize data from JSON file"""
    with open(filename, 'r') as f:
        data = json.load(f)
        return data
