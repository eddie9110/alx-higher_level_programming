#!/usr/bin/python3

def number_keys(a_dictionary):
    no = 0
    _keys = list(a_dictionary.keys())

    for v in _keys:
        no += 1

    return no
