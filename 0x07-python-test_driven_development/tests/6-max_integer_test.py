#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
	"""TestMaxInteger class
	this class is to test the max_integer function from 6-max_integer
	"""
	def test_max_integer(self):
		"""test_max_integer method
		this method tests if the function properly works
		with negative and positive numbers
		"""
		self.assertEqual(max_integer([-100, 1, 230, 20]), 230)
		self.assertEqual(max_integer([0, -1, -34]), 0)
		self.assertEqual(max_integer([420]), 420)
		self.assertEqual(max_integer([1, 0, 3, 2]), 3)

		self.assertAlmostEqual(max_integer([0.34, 6.22, 191.0]), 191.0)
		self.assertAlmostEqual(max_integer([-433.333, -232.01, -1024.222]), -232.01)

		self.assertIsNone(max_integer([]))
