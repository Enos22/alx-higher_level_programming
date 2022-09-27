#!/usr/bin/python3

"""a function that write a text file (UTF8)
and return the number of character written:"""


def read_file(filename=""):
    """write the specified text to file"""
    with open(filename, 'w', encoding="utf-8") as myfile:
        data_written = myfile.write(text)
    return data_written
