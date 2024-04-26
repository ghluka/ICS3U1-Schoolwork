#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Provides 5 functions for completing all 6 parts of Task 3's assignment 
"""

__author__ = "Luka"
__date__ = "2024/04/24"

import math
import random

def square_root(number:float) -> float:
    """Calculates an approximation of the square root of a number using Heron's method"""
    estimate = 5 * 10 ** (math.log(number, 10) / 2 - 1)
    
    while not math.isclose(estimate, number/estimate):
        estimate = (estimate + (number / estimate)) / 2

    return estimate


def digit_product_sum(number:int) -> int:
    """Adds every digit multiplied with every digit in the same number"""
    sum = 0

    for x in str(number):
        for y in str(number):
            sum += int(x) * int(y)
    
    return sum


def text_to_braille(text:str) -> str:
    """Converts lowercase letters and spaces into Braille symbols"""
    out = ""

    for c in text:
        # latin characters to braille if-statement
        if c == "a":
            out += "\u2801"
        elif c == "b":
            out += "\u2803"
        elif c == "c":
            out += "\u2809"
        elif c == "d":
            out += "\u2819"
        elif c == "e":
            out += "\u2811"
        elif c == "f":
            out += "\u280b"
        elif c == "g":
            out += "\u281b"
        elif c == "h":
            out += "\u2813"
        elif c == "i":
            out += "\u280a"
        elif c == "j":
            out += "\u281a"
        elif c == "k":
            out += "\u2805"
        elif c == "l":
            out += "\u2807"
        elif c == "m":
            out += "\u280d"
        elif c == "n":
            out += "\u281d"
        elif c == "o":
            out += "\u2815"
        elif c == "p":
            out += "\u280f"
        elif c == "q":
            out += "\u281f"
        elif c == "r":
            out += "\u2817"
        elif c == "s":
            out += "\u280e"
        elif c == "t":
            out += "\u281e"
        elif c == "u":
            out += "\u2825"
        elif c == "v":
            out += "\u2827"
        elif c == "w":
            out += "\u283a"
        elif c == "x":
            out += "\u282d"
        elif c == "y":
            out += "\u283d"
        elif c == "z":
            out += "\u2835"
        elif c == " ":
            out += " "

    return out


def braille_to_text(text:str) -> str:
    """Converts lowercase Braille symbols and spaces into text"""
    out = ""

    for c in text:
        # braille to latin characters if-statement
        if c == "\u2801":
            out += "a"
        elif c == "\u2803":
            out += "b"
        elif c == "\u2809":
            out += "c"
        elif c == "\u2819":
            out += "d"
        elif c == "\u2811":
            out += "e"
        elif c == "\u280b":
           out += "f"
        elif c == "\u281b":
            out += "g"
        elif c == "\u2813":
            out += "h"
        elif c == "\u280a":
            out += "i"
        elif c == "\u281a":
            out += "j"
        elif c == "\u2805":
            out += "k"
        elif c == "\u2807":
            out += "l"
        elif c == "\u280d":
            out += "m"
        elif c == "\u281d":
            out += "n"
        elif c == "\u2815":
            out += "o"
        elif c == "\u280f":
            out += "p"
        elif c == "\u281f":
            out += "q"
        elif c == "\u2817":
            out += "r"
        elif c == "\u280e":
            out += "s"
        elif c == "\u281e":
           out += "t"
        elif c == "\u2825":
            out += "u"
        elif c == "\u2827":
            out += "v"
        elif c == "\u283a":
            out += "w"
        elif c == "\u282d":
            out += "x"
        elif c == "\u283d":
            out += "y"
        elif c == "\u2835":
            out += "z"
        elif c == " ":
            out += " " 

    return out


def domino_str(domino_1:int, domino_2:int) -> str:
    """Returns a formatted string of two dominos side by side with the parameters being their respective amount of pips"""
    # start grids
    grid_row_1 = "|"
    grid_row_2 = "|"
    grid_row_3 = "|"

    # loops through domino_1 and domino_2
    for domino in f"{domino_1}{domino_2}":
        domino = int(domino)

        if domino == 2 or domino == 3:
            grid_row_1 += "\u25cf    " # top-left pip
            grid_row_3 += "    \u25cf" # bottom-right pip
        elif domino == 4 or domino == 5:
            grid_row_1 += "\u25cf   \u25cf" # top-left and top-right pips
            grid_row_3 += "\u25cf   \u25cf" # bottom-left and bottom-right pips
        elif domino == 6:
            grid_row_1 += "\u25cf \u25cf \u25cf" # top pips
            grid_row_3 += "\u25cf \u25cf \u25cf" # bottom pips
        else:
            grid_row_1 += "     " # empty top
            grid_row_3 += "     " # empty bottom

        if domino == 1 or domino == 3 or domino == 5:
            grid_row_2 += "  \u25cf  " # center pip
        else:
            grid_row_2 += "     " # empty middle
        
        # close rows
        grid_row_1 += "|"
        grid_row_2 += "|"
        grid_row_3 += "|"

    # top of dice
    out = " " + "_" * 11 + " \n"
    
    # add grids to return
    out += f"{grid_row_1}\n{grid_row_2}\n{grid_row_3}\n"
    
    # bottom of dice
    out += " " + "\u203e" * 11 + " "
    
    return out


def tree_box(size:int) -> str:
    """Returns a formatted string of a tree contained in a box.
    
    The foliage will reach the width of the parameter "size",
    while the trunk will reach the height of the parameter "size".
    """
    backslash = "\\"

    # box top:
    out = f"+{'-' * size * 2}+\n"
    
    # foliage:
    for i in range(1, size + 1):
        out += f"|{'/' * i: >{size}}{backslash * i: <{size}}|\n"
    
    # trunk:
    for i in range(1, size + 1):
        # alternate trunk styles ("|}" and "{|")
        if i % 2 == 1:
            out += f"|{'|}': ^{size * 2}}|\n"
        else:
            out += f"|{'{|': ^{size * 2}}|\n"
    
    # box bottom:
    out += f"+{'-' * size * 2}+\n"
    
    return out


def domino_stack(left_base:int, right_base:int, target_points:int) -> str:
    """Plays a game of domino stack with user defined bases and target points"""
    out = ""
    
    points = 0
    current_round = 0
    while points <= target_points:
        current_round += 1
        points = 0 # reset points

        stack = domino_str(left_base, right_base)

        stack_left = left_base
        stack_right = right_base

        # draw dominos
        domino_left = random.randint(1, 6)
        domino_right = random.randint(1, 6)

        # continue with round until neither drawn dominos match with the top of the stack
        while domino_left == stack_left or domino_right == stack_right:
            # add points
            if domino_left == stack_left and domino_right == stack_right:
                points += 5
            else:
                points += 2

            # push drawn dominos to stack
            stack_left = domino_left
            stack_right = domino_right

            stack = f"{domino_str(stack_left, stack_right)}\n{stack}"

            # draw new dominos
            domino_left = random.randint(1, 6)
            domino_right = random.randint(1, 6)
        
        # game summary
        stack += f"\nGame #{current_round} Points: {points}"
        if points <= target_points:
            stack += "\n"
        out += stack

    return out