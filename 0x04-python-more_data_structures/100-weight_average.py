#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    out_put = 0
    dev = 0

    for w in my_list:
        out_put += w[0] * w[1]
        dev += w[1]
    out_put /= dev

    return out_put
