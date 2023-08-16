#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    for ok in matrix:
        for pk in ok:
            if pk == ok[-1]:
                print("{:d}".format(pk))
            else:
                print("{:d}".format(pk), end=' ')
