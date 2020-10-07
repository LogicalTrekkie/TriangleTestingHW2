# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from _triangle import _classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

_NR = "Not a Right Triangle"
_NAT = "Not a Triangle"
_E = "Is an Equalateral"
_I = "Is an Isosceles"
_S = "Is Scalene"
_NS = "Is not Scalene"
_N = "NotATriangle"
_NE = "Is an not Equalateral"
_NI = "Is not Isosceles"

class _TestTriangles(unittest.TestCase):
	# define multiple sets of tests as functions with names that begin

    def test_right_triangle1(self):
        '''Test Right'''
        self.assertEqual(_classify_triangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')
    def test_right_triangle_2(self):
        '''Test Right'''
        self.assertEqual(_classify_triangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')
    def test_right_triangle_3(self):
        '''Test Right'''
        self.assertEqual(_classify_triangle(6, 8, 10), 'Right', '6,8,10 is a right triangle')
    def test_right_triangle_4(self):
        '''Test Right'''
        self.assertEqual(_classify_triangle(5, 4, 3), 'Right', '5,4,3 is a right triangle')
    def test_right_triangle_5(self):
        '''Test Right'''
        self.assertNotEqual(_classify_triangle(1, 1, 1), 'Right', '1,1,1 is NOT a right triangle')
    def test_not_a_triangle_1(self):
        '''Test Not A Triangle'''
        self.assertEqual(_classify_triangle(1, 10, 1), 'NotATriangle', '1,10,1 is Not a triangle')
    def test_not_a_triangle_2(self):
        '''Test Not A Triangle'''
        self.assertEqual(_classify_triangle(1, 5, 2), 'NotATriangle', _NAT)
    def test_not_a_triangle_3(self):
        '''Test Not A Triangle'''
        self.assertEqual(_classify_triangle(6, 5, 1), 'NotATriangle', '6,5,1 is Not a triangle')
    def test_not_a_triangle_4(self):
        '''Test Not A Triangle'''
        self.assertEqual(_classify_triangle(30, 10, 10), _N, _NAT)
    def test_not_a_triangle_5(self):
        '''Test Not A Triangle'''
        self.assertNotEqual(_classify_triangle(4, 3, 2), 'NotATriangle', '4,3,2 is a triangle')
    def test_equilateral_1(self):
        '''Test Equalateral'''
        self.assertEqual(_classify_triangle(2, 2, 2), 'Equilateral', _E)
    def test_equilateral_2(self):
        '''Test Equalateral'''
        self.assertNotEqual(_classify_triangle(3, 3, 2), 'Equilateral', _NE)
    def test_equilateral_3(self):
        '''Test Equalateral'''
        self.assertNotEqual(_classify_triangle(3, 4, 5), 'Equilateral', _NE)
    def test_equilateral_4(self):
        '''Test Equalateral'''
        self.assertNotEqual(_classify_triangle(20, 10, 20), 'Equilateral', _NE)
    def test_equilateral_5(self):
        '''Test Equalateral'''
        self.assertNotEqual(_classify_triangle(1, 2, 2), 'Equilateral', _NE)
    def test_scalene_1(self):
        '''Test Scalene'''
        self.assertEqual(_classify_triangle(21, 20, 19), 'Scalene', _S)
    def test_scalene_2(self):
        '''Test Scalene'''
        self.assertEqual(_classify_triangle(20, 21, 19), 'Scalene', _S)
    def test_scalene_3(self):
        '''Test Scalene'''
        self.assertNotEqual(_classify_triangle(15, 15, 17), 'Scalene', _NS)
    def test_scalene_4(self):
        '''Test Scalene'''
        self.assertNotEqual(_classify_triangle(21, 21, 21), 'Scalene', _NS)
    def test_scalene_5(self):
        '''Test Scalene'''
        self.assertNotEqual(_classify_triangle(21, 15, 21), 'Scalene', _NS)
    def test_isoceles_1(self):
        '''Test Isoceles'''
        self.assertEqual(_classify_triangle(10, 10, 6), 'Isoceles', _I)
    def test_isoceles_2(self):
        '''Test Isoceles'''
        self.assertEqual(_classify_triangle(6, 10, 10), 'Isoceles', _I)
    def test_isoceles_3(self):
        '''Test Isoceles'''
        self.assertEqual(_classify_triangle(10, 6, 10), 'Isoceles', _I)
    def test_isoceles_4(self):
        '''Test Isoceles'''
        self.assertNotEqual(_classify_triangle(10, 6, 7), 'Isoceles', _NI)
    def test_isoceles_5(self):
        '''Test Isoceles'''
        self.assertNotEqual(_classify_triangle(5, 5, 5), 'Isoceles', _NI)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
	