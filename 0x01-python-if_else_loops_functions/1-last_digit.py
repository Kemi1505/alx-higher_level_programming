#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    new = number * -1
    last = new % 10
else:
    last = number % 10
if last < 6:
    print("Last string of", number, "is", last, "and is less than 6 and not 0")
elif last == 0:
    print("Last string of", number, "is", last, "and is 0")
else:
    print("Last string of", number, "is", last, "and is greater than 5")
