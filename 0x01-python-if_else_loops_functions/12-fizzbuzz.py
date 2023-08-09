#!/usr/bin/python3

def fizzbuzz():
    for no in range(1,101):
        if no % 3 == 0 and no % 5 == 0:
            print("FizzBuzz ", end="")
        if no % 3 == 0:
            print("Fizz ", end="")
        if no % 5 == 0:
            print("Buzz ", end="")
        else:
            print(f"{no }", end="")

fizzbuzz()
