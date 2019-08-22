import unittest
from listutil import unique
 
class ListUtilTest(unittest.TestCase):
 
    def test_zero_item_list(self):
        self.assertListEqual( [ ], unique([ ]) )

    def test_single_item_list(self):
        self.assertListEqual( ['hi'], unique(['hi']) )
        self.assertListEqual( [10], unique([10]) )
        self.assertListEqual( [0.5], unique([0.5]) )
        self.assertListEqual( [[1, 'a']], unique([[1, 'a']]))
    
    def test_no_duplicate_item_list(self):
        self.assertListEqual( [1, 'b', 'c'], unique([1, 'b', 'c']) )
        self.assertListEqual( [0, 0.1], unique([0, 0.1]) )
        self.assertListEqual( [[1, 'a'], [2, 'b']], unique([[1, 'a'], [2, 'b']]) )

    def test_one_duplicate_item_list(self):
        self.assertListEqual( ['a'], unique(['a', 'a', 'a', 'a', 'a', 'a']) )
        self.assertListEqual( [1], unique([1, 1, 1, 1, 1, 1, 1, 1, 1]) )
        self.assertListEqual( [0.4], unique([0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]) )
        self.assertListEqual( [[2, 'q']], unique([[2, 'q']]*10000) ) # Extreme case

    def test_two_duplicate_item_list(self):
        self.assertListEqual( ['a', 1], unique(['a', 1, 1, 'a', 'a', 1]) )
        self.assertListEqual( [2, 7], unique([2, 7, 7, 7, 2, 7, 7]) )
        self.assertListEqual( [False, True], unique([False, False, False, True, False]) )
        # Extreme case
        self.assertListEqual( [[2, 'q'], ['w', 3]], unique([[2, 'q'], ['w', 3], [2, 'q'], [2, 'q']]*10000) )

    def test_many_duplicate_item_list(self):
        self.assertListEqual( [1, 2, 'y', 4.1], unique([1, 2, 'y', 4.1, 'y', 2, 1]) )
        self.assertListEqual( ['w', 'x', 'y'], unique(['w', 'w', 'x', 'w', 'y', 'x']) )
        self.assertListEqual( [1, 'b', [1,'b']], unique([1, 1, 'b', 1, 'b', [1,'b'], 'b', [1,'b']]) )
        # Extreme case
        self.assertListEqual( [[7, 'x'], [5, 'y'], 9], unique([[7, 'x'], [7, 'x'], [5, 'y'], 9]*10000) )
    
    def test_non_list(self):
        with self.assertRaises(TypeError):
            unique('abcdefg')
            unique(1024)
            unique(3.1415)
            unique(True)


if __name__ == '__main__':
    unittest.main('listutil_test')
