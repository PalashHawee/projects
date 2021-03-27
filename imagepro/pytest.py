import unittest
import main

class TestMain(unittest.Testcase):
	def test_do_stuff(self):
		test_param=10
		result=main.do_stuff(test_param)
		self.assertIsInstance(result,15)

unittest.main()		