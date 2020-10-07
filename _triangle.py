# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""


def _classify_triangle(_a, _b, _c):

    less = _a < 0 or _b < 0 or _c < 0
    big = _a > 200 or _b > 200 or _c > 200
    ins = not(isinstance(_a, int) and isinstance(_b, int) and isinstance(_c, int))

    if less or big or ins:
        return 'InvalidInput'
    # require that the input values be >= 0 and <= 200

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type


    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (_a >= (_b + _c)) or (_b >= (_a + _c)) or (_c >= (_a + _b)):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    if _a == _b and _b == _c:
        return 'Equilateral'
    elif (_a*_a+_b*_b) == _c*_c or (_c*_c+_b*_b) == _a*_a or (_a*_a+_c*_c) == _b*_b:
        return 'Right'
    elif (_a != _b) and  (_b != _c) and (_a != _c):
        return 'Scalene'

    return 'Isoceles'
