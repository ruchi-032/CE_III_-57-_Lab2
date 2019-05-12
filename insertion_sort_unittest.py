import unittest
from insertion_sort import insertion_sort

class SortTestCase(unittest.TestCase):
    def test_insertion_sort(self):
        values = [8,4,6]
        sorteddata = [4,6,8]
        insertion_sort(values)
        self.assertListEqual(values,sorteddata)

if(__name__=='__main__'):
    unittest.main()
