#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
"""
def last_digit(num):
    last_digit_unsigned = abs(num) % 10
    return -last_digit_unsigned if (num < 0) else last_digit_unsigned
"""
myStr = "Last digit of {} is {} and is {}"
str1 = "greater than 5"
str2 = "0"
str3 = "less than 6 and not 0"
if (number < 0):
    last_digit = abs(number) % 10
else:
    last_digit = number % 10

if (last_digit > 5):
    print(myStr.format(number, last_digit, str1))
elif (last_digit == 0):
    print(myStr.format(number, last_digit, str2))
elif (last_digit < 6):
    print(myStr.format(number, last_digit, str3))
