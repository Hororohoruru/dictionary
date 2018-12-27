# -*- coding: utf-8 -*-
"""
Interactive dictionary based on 'Mastering Python through real-world applications' from Medium

author: Juan Jesus Torre Tresols
e-mail: juan-jesus.torre-tresols@inria.fr
"""

import json


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

    try:
        definition = data[word]
    except KeyError as err:
        raise KeyError("The word does not exist in the dictionary, please try again") from err

    return definition


# Input from user
word_user = input("Enter a word: ")

# Do the thing
print(retrieve_definition(word_user))
