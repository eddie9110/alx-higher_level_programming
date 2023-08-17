#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":

    summ = 0

    for uj in range(1, len(argv)):
        summ += int(argv[uj])

    print(summ)
