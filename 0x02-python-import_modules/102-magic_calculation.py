#!/usr/bin/python3

def magic_calculation(a, b):

    from magic_calculation_102 import add, sub

    if a < b:
        xo = add(a, b)
        for g in range(4, 6):
            xo = add(xo, g)
        return xo

    return sub(a, b)
