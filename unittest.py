import unittest
import cap

class TestCap(unittest.TestCase):

	#Test Case - 1
	def test_one_word(self):
		text='python'
		result = cap.cap_text(text)
		self.assertEqual(result,'Python')


	#Test Case - 2
	def test_multiple_words(self):
		text='monty python'
		result=cap.cap_text(text)
		self.assertEqual(result,'Monty Python')


if __name__ == '__main__':
	unittest.main()
