#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
modulo = 10
if number < 0:
    modulo = -10
if number % modulo > 5:
    print(f"Last digit of {number} is {number % modulo} and is greater than 5")
elif number % modulo == 0:
    print(f"Last digit of {number} is {number % modulo} and is 0")
else:
    print(f"Last digit of {number} is {number % modulo}\
 and is less than 6 and not 0")
