#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
"""
def last_digit(num):
    last_digit_unsigned = abs(num) % 10
    return -last_digit_unsigned if (num < 0) else last_digit_unsigned
"""
if (number < 0):
    last_digit = abs(number) % 10
else:
    last_digit = number % 10
if (last_digit > 5):
    print("Last digit of {} is {} and is greater\
    than 5".format(number, last_digit))
elif (last_digit == 0):
    print("Last digit of {} is {} and is zero".format(number, last_digit))
elif (last_digit < 6):
    print("Last digit of {} is {} and is less\
    than 6 and not zero".format(number, last_digit))
else:
    print("Error")