#!/usr/bin/python3
"""
reading data from one format (CSV) 
and converting it into another format (JSON)
"""
import json
import csv


def convert_csv_to_json(csv_filename):
    """converts CSV file to JSON file"""
    try:
        with open(csv_filename, mode='r', encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        with open('data.json', mode='w', encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        return False
