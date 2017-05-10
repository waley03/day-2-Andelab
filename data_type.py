def data_type(n):
	if type(n) == None:
		return 'no value'
	if type(n) == str:
		return len(n)
	elif type(n) == bool:
		return n
	elif type(n) == int:
		if n < 100:
			return "less than 100"
		elif n == 100:
			return 'equal to 100'
		else:
			return "more than 100"
	elif type(n) == list:
		if len(n) < 3:
			return None
		else:
			return n[2]
# print data_type(True)
import unittest

class Data_type_test(unittest.TestCase):
	def test_data_type(self):
		self.assertEqual(data_type(1), "less than 100")
		self.assertEqual(data_type(100), "equal to 100")
		self.assertEqual(data_type(101), "more than 100")
		self.assertEqual(data_type('julius'), 6)
		self.assertEqual(data_type(True), True)
		self.assertEqual(data_type(False), False)
		self.assertEqual(data_type([1,2,3,4]), 3)
unittest.main()
