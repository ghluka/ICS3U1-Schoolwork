#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Provides 5 functions for computing various tasks, typically formatting their values.
"""

__author__ = "Luka"
__date__ = "2024/03/19"

import random


def day_of_apr_1(year:int) -> str:
    """Returns a string stating the weekday April 1st will fall upon based on any given year"""
    day = (year % 100 // 4 + year // 100 // 4 + year % 100 - 2 * (year // 100) + 13) % 7

    if day == 0:
        weekday = "Sunday"
    elif day == 1:
        weekday = "Monday"
    elif day == 2:
        weekday = "Tuesday"
    elif day == 3:
        weekday = "Wednesday"
    elif day == 4:
        weekday = "Thursday"
    elif day == 5:
        weekday = "Friday"
    elif day == 6:
        weekday = "Saturday"
    
    return weekday


def which_term(month:int, day:int) -> str:
    """Returns a string stating what term any month and day will be based on the 2023-2024 school year
    If the day and month fall outside the ranges of terms 1 - 4, it will return "Summer"
    """
    term = "Summer"

    if month == 9 and day >= 8 or month > 9 and month < 11 or month == 11 and day <= 8:
        term = "Term 1"
    elif month == 11 and day >= 9 or month > 11 or month < 2 or month == 2 and day <= 1:
        term = "Term 2"
    elif month == 2 and day >= 2 or month > 2 and month < 4 or month == 4 and day <= 16:
        term = "Term 3"
    elif month == 4 and day >= 17 or month > 4 and month < 6 or month == 6 and day <= 28:
        term = "Term 4"
    
    return term


def is_factorable(a:int, b:int, c:int) -> bool:
    """Returns a boolean value of whether or not a quadratic equation can be factored"""
    discriminant = (b ** 2 - 4 * a * c) ** .5

    return discriminant == int(discriminant)


def dicey_rolls(sides:int) -> bool:
    """Plays a game of Dicey Rolls with a given number of sides and returns if you won in a boolean"""
    win = True

    roll_1 = random.randint(1, sides)
    roll_2 = random.randint(1, sides)
    roll_3 = random.randint(1, sides*2)

    if roll_1 == roll_2 == 1:
        win = False
    elif roll_1 == roll_2 == sides:
        win = False
    elif roll_1 == 1 and roll_2 == sides or roll_1 == sides and roll_2 == 1:
        win = False
    elif roll_3 == 1:
        win = False
    elif roll_3 >= roll_1 + roll_2:
        win = False
    elif roll_1 % 2 == roll_2 % 2 == roll_3 % 2 == 1:
        win = False

    return win


def exponential_function(a:float, b:float, c:float) -> str:
    """Returns a formatted string of an exponential function and its properties (e.g. increasing, decreasing).
    
    If b is less than 0 it returns "complex function"
    If the graph is constant (X never changes) then it outputs that.
    If there are limitations (i.e. x>0) then those are included in the properties
    """
    properties = f"f(x) = {a}({b}){chr(739)} + {c}"
    if c < 0:
        properties = f"f(x) = {a}({b}){chr(739)} - {abs(c)}"

    if b == 0:
        properties = f"f(x) = {c} {{x{chr(1013)}R | x>0}} (constant)"
    elif b == 1 or a == 0:
        properties = f"f(x) = {a + c} (constant)"
    elif b < 0:
        properties = "complex function"
    else:
        if a > 0:
            if b > 1:
                properties += f" {{y{chr(1013)}R | y>{c}}} (increasing)"
            else:
                properties += f" {{y{chr(1013)}R | y>{c}}} (decreasing)"
        elif a < 0:
            if b > 1:
                properties += f" {{y{chr(1013)}R | y<{c}}} (decreasing)"
            else:
                properties += f" {{y{chr(1013)}R | y<{c}}} (increasing)"

    return properties