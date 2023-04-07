""" Some common ways how to work with json files.
"""
import xml.etree.ElementTree as ET
from os.path import isfile



def store_to_xml(tree: ET,
                 filename: str):
    """ Store element tree object to xml file.

    @param tree: XML element tree instance.
    @param filename: XML file with data.
    """
    with open(filename, 'wb', encoding='utf-8') as wb_handle:
        tree.write(wb_handle)



def load_from_xml(filename: str) -> ET:
    """ Load XML data into element tree.

    @param filename: XML file with data.
    """
    assert isfile(filename)
    return ET.parse(filename)
