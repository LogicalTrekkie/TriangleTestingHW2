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
		
	def testRightTriangle4(self): 
		self.assertEqual(classifyTriangle(5,4,3),'Right','5,4,3 is a right triangle')

	def testRightTriangle5(self):
		self.assertNotEqual(classifyTriangle(1,1,1),'Right','1,1,1 is NOT a right triangle')
		
	def testNotATriangle1(self):
		self.assertEqual(classifyTriangle(1,10,1),'NotATriangle','1,10,1 is Not a triangle')
	def testNotATriangle2(self):
		self.assertEqual(classifyTriangle(1,5,2),'NotATriangle','1,5,2 is Not a triangle')
	def testNotATriangle3(self):
		self.assertEqual(classifyTriangle(6,5,1),'NotATriangle','6,5,1 is Not a triangle')
	def testNotATriangle4(self):
		self.assertEqual(classifyTriangle(30,10,10),'NotATriangle','30,10,10 is Not a triangle')
	def testNotATriangle5(self):
		self.assertNotEqual(classifyTriangle(4,3,2),'NotATriangle','4,3,2 is a triangle')
	def testEquilateral1(self):
		self.assertEqual(classifyTriangle(2,2,2),'Equilateral','2,2,2 is a Equilateral triangle')
	def testEquilateral2(self):
		self.assertNotEqual(classifyTriangle(3,3,2),'Equilateral','3,3,2 is NOT Equilateral triangle')
	def testEquilateral3(self):
		self.assertNotEqual(classifyTriangle(3,4,5),'Equilateral','3,4,5 is NOT Equilateral triangle')
	def testEquilateral4(self):	
		self.assertNotEqual(classifyTriangle(20,10,20),'Equilateral','20,10,20 is NOT Equilateral triangle')
	def testEquilateral5(self):
		self.assertNotEqual(classifyTriangle(1,2,2),'Equilateral','1,2,2 is Not Equilateral triangle')
	def testScalene1(self):
		self.assertEqual(classifyTriangle(21,20,19),'Scalene','21,20,19 is a Scalene triangle')
	def testScalene2(self):	
		self.assertEqual(classifyTriangle(20,21,19),'Scalene','21,20,19 is a Scalene triangle')
	def testScalene3(self):	
		self.assertNotEqual(classifyTriangle(15,15,17),'Scalene','15,15,17 is NOT Scalene triangle')
	def testScalene4(self):
		self.assertNotEqual(classifyTriangle(21,21,21),'Scalene','21,21,21 is Not a Scalene triangle')	
	def testScalene5(self):
		self.assertNotEqual(classifyTriangle(21,15,21),'Scalene','21,15,21 is Not a Scalene triangle')		
	def testIsoceles1(self): 
		self.assertEqual(classifyTriangle(10,10,6),'Isoceles','10,10,6 is a Isoceles triangle')
	def testIsoceles2(self): 
		self.assertEqual(classifyTriangle(6,10,10),'Isoceles','10,10,6 is a Isoceles triangle')
	def testIsoceles3(self): 
		self.assertEqual(classifyTriangle(10,6,10),'Isoceles','10,10,6 is a Isoceles triangle')
	def testIsoceles4(self): 
		self.assertNotEqual(classifyTriangle(10,6,7),'Isoceles','10,6,7 is not a Isoceles triangle')
	def testIsoceles5(self): 
		self.assertNotEqual(classifyTriangle(5,5,5),'Isoceles','10,6,7 is not a Isoceles triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

