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

    
    def test_have_duplicate_item_list(self):
        self.assertListEqual( [1, 2, 'y', 4.1], unique([1, 2, 'y', 4.1, 'y', 2, 1]) )
        self.assertListEqual( ['w', 'x', 'y'], unique(['w', 'w', 'x', 'w', 'y', 'x']) )
        self.assertListEqual( [1, 'b', [1,'b']], unique([1, 1, 'b', 1, 'b', [1,'b'], 'b', [1,'b']]) )
        self.assertListEqual( [[7, 'x'], [5, 'y']], unique([[7, 'x'], [5, 'y'], [5, 'y'], [7, 'x']]) )


if __name__ == '__main__':
    unittest.main('listutil_test')
