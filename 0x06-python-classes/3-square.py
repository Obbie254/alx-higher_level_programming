#!/usr/bin/python3
"""creating class with a method"""


class Square:
    """this is class square"""

    def __init__(self, size=0):
        """initialization of the class"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """method that works out area from size"""

        return (self.__size**2)
