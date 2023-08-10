#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

no = abs(number) % 10

if number < 0:
    no = -no

com = line = "Last digit of {} is {} and is {}"

if no > 5:
    print(com.format(number, no, "greater than 5"))
elif no < 6 and no != 0:
    print(com.format(number, no, "less than 6 and not 0"))
else:
    print("Last digit of {} is {} and is 0".format(number, no))
