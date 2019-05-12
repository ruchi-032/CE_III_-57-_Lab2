import unittest
from merge_sort import mergeSort

class SortTestCase(unittest.TestCase):
    def test_merge_sort(self):
        values = [5,3,6]
        sorteddata = [3,5,6]
        mergeSort(values, 0, len(values) - 1)
        print(values)
        self.assertListEqual(values,sorteddata)

if(__name__=='__main__'):
    unittest.main()