#!/usr/bin/python3
"""This is to make a change
"""


def makeChange(coins, total):
    """ function with two argument """
    if total <= 0:
        return 0
    temp_value = 0
    
    coins.sort(reverse=True)

    for coin in coins:
        while total >= coin:
            total -= coin
            temp_value += 1

    return temp_value if total == 0 else -1
