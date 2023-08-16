#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    divdnd = []
    for a in my_list:
        divdnd.append(True if a % 2 == 0 else False)
    return divdnd
