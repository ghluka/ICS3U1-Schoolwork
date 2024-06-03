"""Provides 5 functions for completing all 6 parts of Task 3's assignment 
"""

__author__ = "Luka"
__date__ = "2024/06/03"


def get_closest(sequence:list, target:int) -> int:
    closest = sequence[0]
    for v in sequence:
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