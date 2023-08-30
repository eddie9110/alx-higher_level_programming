#!/usr/bin/python3
import dis


def magic_calculation(a, b):
    result = 0

    for nu in range(1, 3):
        try:
            if nu > a:
                raise Exception("Too far")
            result += (a ** b) / nu

        except Exception:
            result = a + b
            break

    return result
