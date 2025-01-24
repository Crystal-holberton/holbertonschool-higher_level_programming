#!/usr/bin/python3
"""prints a text"""


def text_indentation(text):
    """
    Print text with two new lines after each '.', '?', and ':'

    Args:
        text (str): text to print
    Raises:
        TypeError: text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1
    while i < len(text):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
