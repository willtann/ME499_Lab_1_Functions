#! /Users/tannerwilliams/Desktop/ME 499/ME499_Lab_1_Functions
from math import gcd as pygcd
# Problem statement instructions
from gcd import pygcd
# For testing
from random import randint


# SECOND TRY
def gcd(a, b):
    remainder = 1  # Giving the loop the something to start with
    # If one number is zero then gcd is the other
    if a == 0 or b == 0:
        return max(a, b)
    while remainder != 0:
        remainder = max(a, b) % min(a, b)  # Divide small number out of larger number
        a = min(a, b)  # small number acts as place-holder for next go-around
        b = remainder  # We want this to be zero
    else:
        return a


def gcd_test():
    for _ in range(1000):
        a = randint(1, 1000)
        b = randint(1, 1000)
        if pygcd(a, b) == gcd(a, b):
            return True
        else:
            return False


print(gcd_test())
