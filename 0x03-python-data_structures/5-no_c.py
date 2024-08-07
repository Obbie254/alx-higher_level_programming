#!/usr/bin/python3
"""
Method 1
By creating a dict
"""


def no_c(my_string):
    my_string = my_string.translate({ord(i): None for i in 'Cc'})
    return (my_string)

"""
Method 2
By creating a table

def no_c(my_string):
	my_string = my_string.translate(str.maketrans("", "", "cC"))
	print(my_string)
"""
