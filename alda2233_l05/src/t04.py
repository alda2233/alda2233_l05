"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-10-20"
-------------------------------------------------------
"""
# Imports
from functions import closest
# Constants


def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """


close = None
target = float(input("target: "))
v1 = float(input("v1: "))
v2 = float(input("v2: "))

result = closest(target, v1, v2)
print(result)
