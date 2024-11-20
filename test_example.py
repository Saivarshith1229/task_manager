import unittest

class TestBasicFunctions(unittest.TestCase):
    def test_addition(self):
        result = 2 + 2
        self.assertEqual(result, 4, "Basic addition test failed")
    
    def test_string_upper(self):
        text = "hello"
        result = text.upper()
        self.assertEqual(result, "HELLO", "String uppercase conversion failed")
    
    def test_list_length(self):
        test_list = [1, 2, 3, 4, 5]
        self.assertEqual(len(test_list), 5, "List length test failed")

if __name__ == '__main__':
    unittest.main() 