#!/usr/bin/python3
"""
A function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """function that print complete name"""
    if type(first_name) is not str or first_name == "":
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    """print(f"{My name is {first_name} {last_name}")"""
    print("My name is {} {}".format(first_name, last_name))
