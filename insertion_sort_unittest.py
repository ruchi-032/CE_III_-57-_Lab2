import unittest
from insertion_sort import insertion_sort

class SortTestCase(unittest.TestCase):
    def test_insertion_sort(self):
        values=[5,3,6]
        sorteddata=[3,5,6]
        insertion_sort(values)
        self.assertListEqual(values,sorteddata)

if(__name__=='__main__'):
    unittest.main()