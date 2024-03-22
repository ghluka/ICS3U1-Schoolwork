#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Provides 5 functions for computing various tasks, typically formatting their values.
"""

__author__ = 'Luka'
__date__ = '2024/02/28'


def near_pi() -> float:
    """Returns an approximation of pi, accurate to ten digits"""
    return (63/25)*((17 + 15 * (5 ** 0.5)) / (7 + 15 * (5 ** 0.5)))


def easter_date(year:int) -> str:
    """Returns the date (in yy/mm/dd format) of when Easter will be for any given year"""
    # Computus algorithm
    a = year % 19
    b = year // 100
    c = year % 100
    e = (8 * b + 13) // 25
    f = (19 * a + b - (b // 4) - e + 15) % 30
    g = (32 + 2 * (b % 4) + 2 * (c // 4) - f - (c % 4)) % 7
    h = (a + 11 * g + 19 * g) // 433

    month = (f + g - 7 * h + 90) // 25
    day = (f + g + 33 * month + 19) % 32

    return f"{year}/{month:0>2}/{day:0>2}"


def age_difference(name_1:str, age_1:int, name_2:str, age_2:int) -> str:
    """Returns a formatted string of the age difference of two people"""
    difference = ((age_2-age_1)**2)**.5
    
    return f"[{name_1:.<12}vs{name_2:.>12}]-->{difference:.0f} apart"


def seconds_converter(seconds:int) -> str:
    """Converts seconds into years, days, hours, minutes and remaining seconds in a formatted string"""
    m = seconds // 60
    s = seconds % 60

    h = m // 60
    m = m % 60

    d = h // 24
    h = h % 24

    y = d // 365
    d = d % 365

    return f"{y}y_{d:_>3}d_{h:_>2}h_{m:_>2}m_{s:_>2}s"


def near_sine(degrees:float) -> float:
    """Returns the sine of a specified angle in degrees using Bhaskara I's sine approximation formula"""
    pi_approx = near_pi()
    radians = (degrees * pi_approx) / 180

    return (16 * radians * (pi_approx - radians)) / (5 * pi_approx ** 2 - 4 * radians * (pi_approx - radians))