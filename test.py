import unittest

from  three_five_multiple import sum_multiples

class TestMultiple(unittest.TestCase):
    #tests if the test function is working properly
    #three cases - bounds of 23,33,45
    def test_sum(self):
        self.assertEqual(23, sum_multiples(10))
        self.assertEqual(33, sum_multiples(11))
        self.assertEqual(45, sum_multiples(13))

    #assumes sum passed all tests
    #assumes bash file was run
    #makes sure files have been written and it's correct
    def test_main(self):
        first = int(open('test.txt', 'r').readline())
        self.assertEqual(5829168, first)
        second = int(open('test1.txt', 'r').readline())
        self.assertEqual(23, second)
        third = int(open('test2.txt', 'r').readline())
        self.assertEqual(9168, third)

#run it
if __name__ == '__main__':
    unittest.main()
