#! /Users/tannerwilliams/Desktop/ME 499/ME499_Lab_1_Functions
import math


def close(aa, bb, diff):
    actual = abs(float(aa-bb))
    if actual < diff:
        tf = True
    else:
        tf = False
    return tf


# print(close(1, 2, 3))
# print(close(1, 2, 0.5))
