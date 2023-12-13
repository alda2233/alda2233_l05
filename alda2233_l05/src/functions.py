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
from math import fabs
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


def magic_date(day, month, year):
    """
    -------------------------------------------------------
    Determines if a date is magic. A date is magic if the day
    times the month equals the year.
    Use: magic = magic_date(day, month, year)
    -------------------------------------------------------
    Parameters:
        day - numeric day (int > 0)
        month - numeric month (int > 0)
        year - numeric two-digit year (int > 0)
    Returns:
        magic - True if date is magic, False otherwise (boolean)
    -------------------------------------------------------
    """

    product = day*month
    if product == year:
        magic = True
    else:
        magic = False

    return magic


def closest(target, v1, v2) -> float:
    """
    -------------------------------------------------------
    Determines closest value of two values to a target value.
    Use: result = closest(target, diff_v1, diff_v2)
    -------------------------------------------------------
    Parameters:
        target - the target value (float)
        diff_v1 - first comparison value (float)
        diff_v2 - second comparison value (float)
    Returns:
        result - one of diff_v1 or diff_v2 that is closest to target,
          diff_v1 is the value chosen if diff_v1 and diff_v2 are an equal
          distance from target (float)
    -------------------------------------------------------
    """

    diff_v1 = abs(target - v1)
    diff_v2 = abs(target - v2)

    if diff_v1 <= diff_v2:
        result = v1
    else:
        result = v2

    return float(result)


def roman_numeral(n):
    """
    -------------------------------------------------------
    Convert 1-10 to Roman numerals.
    Use: numeral = roman_numeral(n)
    -------------------------------------------------------
    Parameters:
        n - number to convert to Roman numerals (int)
    Returns:
        numeral - Roman numeral version of n, None if n is not
          between 1 and 10 inclusive. (str)
    -------------------------------------------------------
    """

    if n == 1:
        numeral = "I"
    elif n == 2:
        numeral = "II"
    elif n == 3:
        numeral = "III"
    elif n == 4:
        numeral = "IV"
    elif n == 5:
        numeral = "V"
    elif n == 6:
        numeral = "VI"
    elif n == 7:
        numeral = "VII"
    elif n == 8:
        numeral = "VIII"
    elif n == 9:
        numeral = "IX"
    elif n == 10:
        numeral = "X"
    else:
        n = None

    return str(numeral)


def pay_raise(status, years, salary):
    """
    -------------------------------------------------------
    Calculates pay raises for employees. Pay raises are based on:
    status: Full Time ('F)' or Part Time ('P')
    and years of service
    Raises are:
        5% for full time greater than or equal to 10 years service
        1.5% for full time less than 4 years service
        3% for part time greater than 10 years service
        1% for part time less than 4 years service
        2% for all others
    Use: new_salary = pay_raise(status, years, salary)
    -------------------------------------------------------
    Parameters:
        status - employment type (str - 'F' or 'P')
        years - number of years employed (int > 0)
        salary - current salary (float > 0)
    Returns:
        new_salary - employee's new salary (float).
    -------------------------------------------------------
    """

    FTEN = 0.05
    FFOUR = 0.015
    PTEN = 0.03
    PFOUR = 0.01
    OTHER = 0.02

    if status == 'F' and years >= 10:
        new_salary = (salary*FTEN) + salary
    elif status == 'F' and years < 4:
        new_salary = (salary*FFOUR) + salary
    elif status == 'P' and years > 10:
        new_salary = (salary * PTEN) + salary
    elif status == 'P' and years < 4:
        new_salary = (salary*PFOUR) + salary
    else:
        new_salary = (salary*OTHER) + salary

    return float(new_salary)


def ticket():
    """
    -------------------------------------------------------
    School play ticket price calculation.
    Asks user for their age, and if necessary, if they are
    a student at the school. Prices:
        Infant (age < 3): $0
        Senior (age >= 65): $4.00
        Student (10 <= age < 18): $3.00
            Student of this school: $1.00
        Adult (18 <= age < 65): $5.00
        Kid (3 <= age < 10): $2.00
    Use: price = ticket()
    -------------------------------------------------------
    Returns:
        price - the price of one ticket (float)
    -------------------------------------------------------
    """

    INFANT = 2
    KID_MIN_AGE = 3
    KID_MAX_AGE = 9
    STUDENT_MIN_AGE = 10
    STUDENT_MAX_AGE = 17
    ADULT_MIN_AGE = 18
    ADULT_MAX_AGE = 64
    SENIOR_MIN_AGE = 65

    age = int(input("Enter your age: "))

    if age < INFANT:
        price = 0
    elif age >= SENIOR_MIN_AGE:
        price = 4.00
    elif STUDENT_MIN_AGE <= age <= STUDENT_MAX_AGE:
        student = input("Are you a student at the school (Y/N)? ")
        if student == 'Y':
            price = 1.00
        else:
            price = 3.00
    elif KID_MIN_AGE <= age <= KID_MAX_AGE:
        price = 2.00
    else:
        price = 5.00

    return float(price)
