#!/usr/bin/python3

def uppercase(str):
    for xo in str:
        if ord(xo) >= 97 and ord(xo) <= 122:
            xo = chr(ord(xo) - 32)
        print("{}".format(xo), end="")
    print("")
