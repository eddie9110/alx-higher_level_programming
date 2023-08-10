#!/usr/bin/python3

def remove_char_at(str, n):
    nstr = ""
    for idx in range(0, len(str)):
        if idx != n:
            nstr += str[idx]
    return nstr
