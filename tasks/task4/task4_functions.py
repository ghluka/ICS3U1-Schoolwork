"""Provides solutions for the 8 functions in Task 4's assignment 
"""

__author__ = "Luka"
__date__ = "2024/06/10"

import random


def get_closest(values:list, target:int) -> int:
    """Returns the closest number from a list of values to a target"""
    closest = values[0]

    for v in values:
        if abs(target - v) < abs(target - closest):
            closest = v
    
    return closest


def get_closest_pair(sequence_1:list, sequence_2:list) -> int:
    closest_i = 0
    closest = abs(sequence_1[closest_i] - sequence_2[closest_i])

    for i in range(0, len(sequence_1)):
        v = sequence_1[i]
        target = sequence_2[i]

        if abs(target - v) < abs(target - closest):
            closest = abs(target - v)
            closest_i = i

    return [sequence_1[closest_i], sequence_2[closest_i]]


def get_proper_divisors(number:int) -> list:
    """
    Returns a list of the proper divisors (divisors of a number excluding
    itself) of a number.
    """
    divisors = []

    for n in range(number // 2, 0, -1):
        if number % n == 0:
            divisors.append(n)

    return divisors

def rolling_averages(values:list, size:int) -> list:
    """
    Returns a list of the rolling averages of a list of values
    with a given size.
    """
    averages = []
    
    for i in range(len(values) - size + 1):
        average = []

        for a in range(size):
            average.append(values[i + a])

        averages.append(sum(average) / size)

    return averages


def align_strings(strings:list, substr:str) -> str:
    """
    Returns a string of an aligned list of strings by a substring,
    ignores all strings without the substring.

    Example:
    >>> words = ["mathematics", "radius", "theorem", "breathe", "apothem", "area"]
    >>> print(align_strings(words, "The"))
      maTHEhematics
        THEheorem  
    breaTHEhe      
     apoTHEhem     
    """
    left = []
    padding_l = 0
    right = []
    padding_r = 0

    for string in strings:
        i = string.lower().find(substr.lower())
        if i != -1:
            left.append(string[:i])
            right.append(string[i + 1:])

            if len(left[-1]) > padding_l:
                padding_l = len(left[-1])
            if len(right[-1]) > padding_r:
                padding_r = len(right[-1])

    out = ""
    
    for i in range(len(left)):
        out += f"{left[i].lower(): >{padding_l}}{substr.upper()}{right[i]: <{padding_r}}\n"

    return out[:-1] # remove trailing new-line

def make_decks(num_decks: int) -> str: # provided by assignment
    """
    Returns a list of 2-character cards for num_decks standard card decks,
    ordered by value (A to K) and suit (♠, ♣, ♥, ♦).
    """
    deck = []

    for c in 'A23456789TJQK':
        for s in '♠♣♥♦':
            deck.extend([f'{c}{s}']*num_decks)

    return deck


def deal_n_cards(cards:list, n:int) -> list:
    """
    Returns the first n cards from the list "cards" as a new list,
    removes the first n cards from the list "cards".
    """
    hand = []

    if len(cards) - n < 0:
        n = len(cards)

    for _ in range(n):
        hand.append(cards[0])
        cards.pop(0)

    return hand


def cut_the_cards(cards:list) -> None:
    """Cuts a list in two halfs from a random position and merges them."""
    temp_cards = cards.copy()

    i = random.randrange(len(cards))
    cards.clear()
    cards.extend(temp_cards[i:])
    cards.extend(temp_cards[:i])
    

def shuffler(values:list) -> list:
    # cut the deck
    i = random.randrange(len(values))
    left = values[:i]
    right = values[i:]

    # merge decks
    merged = []

    while len(left) > 0 and len(right) > 0:
        if random.randrange(0, 2) == 0:
            merged.append(left[0])
            left.pop(0)
        else:
            merged.append(right[-1])
            right.pop(-1)
    
    # place remaining cards
    merged.extend(left)
    merged.extend(right)

    return merged