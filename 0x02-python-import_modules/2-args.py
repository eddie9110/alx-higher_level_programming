#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    print("{} {}{}{}".format(len(argv) - 1,
          "argument", "s" if len(argv) - 1 != 1 else "",
                             ":" if len(argv) - 1 > 0 else "."))

    for ko in range(1, len(argv)):
        print("{}: {}".format(ko, argv[ko]))
