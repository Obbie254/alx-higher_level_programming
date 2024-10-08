#!/usr/bin/python3
""" Return true if the object is an instance of a class """


def is_same_class(obj, a_class):
    """
    Return true if the object is an instance of a class
    """
    return type(obj) is (a_class)
