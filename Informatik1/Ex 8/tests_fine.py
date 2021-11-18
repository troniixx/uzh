#!/usr/bin/env python3
from unittest import TestCase
from public.script import fine_calculator

# Implement this test suite. Make sure that you define test
# methods and that each method _directly_ includes an assertion
# in the body, or -otherwise- the grading will mark the test
# suite as invalid.
class FineCalculatorTest(TestCase):
    
	def test_area_type(self):
		expected ="Invalid Area Type"
		actual = fine_calculator(12, 40)
		self.assertEqual(expected, actual)
		
	def test_area_value(self):
		expected ="Invalid Area Value"
		actual = fine_calculator("highway", 30)
		self.assertEqual(expected, actual)
	
	def test_speed_type(self):
		expected = "Invalid Speed Type"
		actual = fine_calculator("urban", [12, 45])
		self.assertEqual(expected, actual)
	
	def test_speed_value(self):
		expected ="Invalid Speed Value"
		actual = fine_calculator("motorway", -12)
		self.assertEqual(expected, actual)
	
	def test_below_limit(self):
		expected = 0
		actual = fine_calculator("expressway", 95)
		self.assertEqual(expected, actual)
	
	def test_urban_60(self):
		expected = round(1*20**2)
		actual = fine_calculator("urban", 60)
		self.assertEqual(expected, actual, 0)
	
	def test_expressway_110(self):
		expected = round(0.8*10**2)
		actual = fine_calculator("expressway", 110)
		self.assertEqual(expected, actual, 0)
	
	def test_motorway_180(self):
		expected = round(0.5*50**2)
		actual= fine_calculator("motorway", 180)
		self.assertEqual(expected, actual, 0)
	
	def test_fine_type(self):
		actual = fine_calculator("expressway", 118)
		self.assertIsInstance(actual, int)
	
	