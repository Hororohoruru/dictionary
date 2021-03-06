# -*- coding: utf-8 -*-
"""
Interactive dictionary based on 'Mastering Python through real-world applications' from Medium

author: Juan Jesus Torre Tresols
e-mail: juan-jesus.torre-tresols@inria.fr
"""

import json

from difflib import get_close_matches
from pprint import pprint


# Load data
with open('dictionary.json', 'r') as dictionary:
    data = json.load(dictionary)


def retrieve_definition(word):
    """Gives the definition of the word given as output

    Parameters
    ----------

    word: str
          dict key containing the definition requested by the function call

    Returns
    -------

    definition: str
                definition of the word requested y the function call
    """

    if word in data:
        definition = data[word]
    elif word.title() in data:
        definition = data[word.title()]
    elif word.upper() in data:
        definition = data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        closest = get_close_matches(word, data.keys())[0]
        action = input("Did you mean %s instead? [y/n]: " % closest)

        if action.lower() == "y":
            definition = data[closest]
        elif action.lower() == "n":
            definition = "The word does not exist yet"
        else:
            definition = "I do not understand, please try again"

    else:
        definition = "The word doesn't exist, please double check it"

    return definition


# Input from user
word_user = input("Enter a word: ").lower()

# Do the thing
output = retrieve_definition(word_user)

# Print each definition in one line
for item in output:
    print("-", item)
