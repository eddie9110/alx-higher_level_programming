#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    n_list = []
    for x, y in a_dictionary.items():
        if value is y:
            n_list.append(x)
    for i in reversed(n_list):
        del a_dictionary[i]
    return a_dictionary
