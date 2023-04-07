""" Some common ways how to work with json files
"""
import json



def store_to_json(dictionary: dict,
                  filename: str):
    """ Store dictionary to json file.

    @param dictionary: Input dictionary to store.
    @param filename: Filename.
    """
    with open(filename, 'w', encoding='utf--8') as w_handle:
        json.dump(dictionary,
                  w_handle,
                  indent=4,
                  sort_keys=False)



def load_from_json(filename: str) -> dict:
    """ Load data from json into a dictionary.

    @param filename: JSON file name.

    @returns Dictionary filled with filename data.
    """
    with open(filename, 'r', encoding='utf-8') as r_handle:
        return json.load(r_handle)
