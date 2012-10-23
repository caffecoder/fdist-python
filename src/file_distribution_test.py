#!/usr/bin/env python

import unittest
import os.path

from file_distribution import FileDistribution

__author__ =  'Adam Kubica (caffecoder) <caffecoder@kaizen-step.com>'

class TestFileDistribution(unittest.TestCase):
	def setUp(self):
		self.fd = FileDistribution("/tmp//")

	def testPath(self):
		self.assertEqual(self.fd.get_path(), "/tmp")

	def testCase1(self):
		self.fd.set_extension("tmp")
		self.fd.set_extension(".dat")
		self.fd.hex_path(102423)
		self.assertEqual(self.fd.get_path(), "/tmp/01/90/17.dat")

	def testCase2(self):
		self.fd.set_extension("dat")
		self.fd.hex_path(256)
		self.assertEqual(self.fd.get_path(), "/tmp/01/00.dat")

	def testCase3(self):
		self.fd.set_extension("")
		self.fd.hex_path(256)
		self.assertEqual(self.fd.get_path(), "/tmp/01/00")

	def testcase4(self):
		self.fd.hex_path(1)
		self.assertEqual(self.fd.get_path(), "/tmp/01.dat")

	def testCase5(self):
		f = open('/tmp/test.txt', 'w')
		f.close()
		
		self.assertTrue(os.path.exists("/tmp/test.txt"))

		self.fd.set_extension(".dat")
		self.fd.hex_path(256)

		self.fd.rename_from("/tmp/test.txt")
		self.assertTrue(os.path.exists("/tmp/01/00.dat"))

	def tearDown(self):
		pass

if __name__ == '__main__':
    unittest.main()