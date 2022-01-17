#! /Users/tannerwilliams/Desktop/ME 499/ME499_Lab_1_Functions
import math


# Function calculating the volume of a cylinder
def cylinder_volume(radius, height):
    if radius > 0 and height > 0:
        return (math.pi * (float(radius) ** 2)) * float(height)
    else:
        raise ValueError


# Function calculating the volume of a torus
def torus_volume(inner_rad, outer_rad):
    if 0 < inner_rad < outer_rad and outer_rad > 0:
        return 0.25 * (math.pi ** 2) * (float(inner_rad) +
                                        float(outer_rad)) * ((float(outer_rad) - float(inner_rad)) ** 2)
    else:
        raise ValueError


# print(cylinder_volume(-2, 3))
# print(cylinder_volume(2, 3))
#
# print(torus_volume(-2, 3))
# print(torus_volume(2, 3))
