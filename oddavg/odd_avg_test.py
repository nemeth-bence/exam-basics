import unittest
from odd_avg import odd_average

class TestOddAverage(unittest.TestCase):

    def test_average_with_empty_list(self):
        list = []
        object1 = odd_average()
        self.assertEqual(object1(list), 0)

    def test_average_with_one_element(self):
        list = [5]
        object1 = odd_average()
        self.assertEqual(object1(list), 5)

    def test_average_with_null(self):
        list = [0]
        object1 = odd_average()
        self.assertEqual(object1(list), 0)

if __name__ == '__main__':
    unittest.main()
