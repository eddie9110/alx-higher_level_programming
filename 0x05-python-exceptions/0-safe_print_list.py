#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    cnt = 0
    for bo in range(x):
        try:
            print(my_list[bo], end="")
            cnt += 1
        except IndexError:
            break
    print("")
    return cnt
