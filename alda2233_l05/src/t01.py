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
from functions import magic_date
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


day = int(input("day: "))
month = int(input("month: "))
year = int(input("year: "))
magic = magic_date(day, month, year)

print(magic)
