"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-10-19"
-------------------------------------------------------
"""
# Imports
from functions import pay_raise
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


status = input("F or P: ")
years = float(input("Years: "))
Salary = float(input("Salary: "))

new_salary = pay_raise(status, years, Salary)

print(f"{new_salary:.2f}")
