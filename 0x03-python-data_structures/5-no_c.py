#!/usr/bin/python3

def no_c(my_string):
    n_str = ''
    for xc in my_string:
        if xc != 'c' and xc != 'C':
            n_str = n_str + xc
    return n_str
