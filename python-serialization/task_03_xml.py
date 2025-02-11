#!/usr/bin/python3
"""serialization and deserialization using XML"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    should serialize the dictionary into XML
    and save it to the given filename
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    with open(filename, 'wb') as xml_file:
        tree.write(xml_file)

def deserialize_from_xml(filename):
    """
    take a filename as its parameter, read the XML data,
    return a deserialized Python dictionary
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {child.tag: child.text for child in root}
    return result
