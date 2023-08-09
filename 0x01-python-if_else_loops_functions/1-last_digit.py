#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

no = abs(number) % 10

if number < 0:
    no = -no

if no > 5:
    print(f"Last digit of {number} is {no} and is is greater than 5")
elif no == 0:
    print(f"Last digit of {number} is {no} and is 0")
else:
    print(f"Last digit of {number} is {no} and is less than 6 and not 0")
