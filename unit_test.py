

import unittest


def add_2(number):
    return number + 2

def concatenate(string1, string2):
    return string1 + string2

def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False
    
class PracticeTestCase(unittest.TestCase):
    
    def test_5_odd(self):
        self.assertTrue(is_odd(5))
        
    def test_14_even(self):
        self.assertFalse(is_odd(14))
        
    def test_concatenate(self):
        self.assertEqual(concatenate("test ","successful"), "test successful")
        
    def test_negative_one_add_2(self):
        self.assertEqual(add_2(-1), 1)



if __name__ == "__main__":
    print('Unit tests are running')
    unittest.main()
