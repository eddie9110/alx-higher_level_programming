#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    n_lst = []
    for xo in range(len(my_list)):
        n_lst.append(element if xo == idx else my_list[xo])
    return n_lst
