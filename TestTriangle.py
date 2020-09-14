# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangle1(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangle2(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testRightTriangle3(self): 
        self.assertEqual(classifyTriangle(6,8,10),'Right','6,8,10 is a right triangle')
		
    def testRightTriangle3(self): 
        self.assertEqual(classifyTriangle(5,4,3),'Right','5,4,3 is a right triangle')

	def testRightTriangle3(self): 
        self.assertNotEqual(classifyTriangle(1,1,1),'Right','1,1,1 is NOT a right triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

