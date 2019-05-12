import unittest
from merge_sort import mergeSort

class SortTestCase(unittest.TestCase):
    def test_merge_sort(self):
        values = [8,4,6]
        sorteddata = [4,6,8]
        mergeSort(values, 0, len(values) - 1)
        print(values)
        self.assertListEqual(values,sorteddata)

if(__name__=='__main__'):
    unittest.main()
