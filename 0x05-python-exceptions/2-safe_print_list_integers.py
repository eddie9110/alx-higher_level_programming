#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    cnt = 0

    for bo in range(x):
        try:
            print("{:d}".format(my_list[bo]), end="")
            cnt += 1

        except (TypeError, ValueError):
            break
    print("")

    return cnt
