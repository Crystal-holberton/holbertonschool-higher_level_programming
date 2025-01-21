#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    
    roman_nums = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    results = 0
    last_value = 0

    for number in reversed(roman_string):
        value = roman_nums[number]
        if value < last_value:
            results -= value
        else:
            results += value
        last_value = value
    return results
