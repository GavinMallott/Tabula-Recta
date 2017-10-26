"""
Tabula Recta
--Managing Key File--

Author: Gavin Mallott
Created: July 20, 2017
Lasted Edited: October 24, 2017
Last Edit: Adding docstrings/annotations
"""


import re


def write_key_file(key_file):
    """Opens key.txt and writes to it"""

    key_file = open("key.txt", 'w+')
    key_file.write(key_file)
    key_file.close()


def read_key_file():
    """Reads key from key.txt"""

    key_file = open("key.txt", 'r+')
    key_text = key_file.read()
    key_file.close()
    return key_text


def stripper(text):
    """Strips all punctuation and spaces from the key data and returns it in uppercase"""

    key_text = text
    key_text = re.sub('[\s+\d+\W+]', '', key_text)
    key = key_text.upper()
    return key


key = stripper(read_key_file())


if __name__ == '__main__':
    print(key)