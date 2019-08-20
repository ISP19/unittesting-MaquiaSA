import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_init(self):
        with self.assertRaises(ValueError):
            Fraction(0, 0)
        with self.assertRaises(TypeError):
            Fraction(0.1, 8)
            Fraction(12, 1.3)
            Fraction('a', 4)
            Fraction(18, 'b')
            Fraction(True, 4)
            Fraction(2, False)


    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        f = Fraction(-75, -150)
        self.assertEqual("1/2", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())
        f = Fraction(10, 0)
        self.assertEqual("1/0", f.__str__())
        f = Fraction(-50, 0)
        self.assertEqual("-1/0", f.__str__())


    # TODO Write tests for __init__, __eq__, +, *.
    # Here is an example, but you must add more test cases.  
    # The test requires that your __eq__ is correct.
    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3, 4), Fraction(1, 12) + Fraction(2, 3))
        # 1/2 = 6/8 + (-1/4)
        self.assertEqual(Fraction(1, 2), Fraction(6, 8) + Fraction(-1, 4))
        # -4/5 = (-1/10) + (-3/10) + (-2/5)
        self.assertEqual(Fraction(-4, 5), Fraction(-1, 10) + Fraction(-3, 10) + Fraction(-2, 5))
        # 1/3 = 2/6 + 0/5
        self.assertEqual(Fraction(1, 3), Fraction(2, 6) + Fraction(0, 5))
        # 1/0 = -7/8 + 4/0
        self.assertEqual(Fraction(1, 0), Fraction(-7, 8) + Fraction(4, 0))
        # -1/0 = 3/5 + (-2/0)
        self.assertEqual(Fraction(-1, 0), Fraction(3, 5) + Fraction(-2, 0))
        # 0/0(ValueError) = 4/0 + (-1/0)
        with self.assertRaises(ValueError):
            Fraction(4, 0) + Fraction(-1, 0)
    
    def test_sub(self):
        # 1/5 = 1 - 4/5
        self.assertEqual(Fraction(1, 5), Fraction(1) - Fraction(4, 5))
        # -1 = -2/3 - 7/8
        self.assertEqual(Fraction(-1), Fraction(-2, 3) - Fraction(7, 8) - Fraction(-13, 24))
        # 9/8 = 5/8 - (-1/2)
        self.assertEqual(Fraction(9, 8), Fraction(5, 8) - Fraction(-1, 2))
        # -3/4 = 0 - 3/4
        self.assertEqual(Fraction(-3, 4), Fraction(0) - Fraction(3, 4))
        # 2/7 = 2/7 - 0/3
        self.assertEqual(Fraction(2, 7), Fraction(2, 7) - Fraction(0, 3))
        # 0 = 0/2 - 0/6
        self.assertEqual(Fraction(0), Fraction(0, 2) - Fraction(0, 6))
        # -1/0 = 7/8 - 4/0
        self.assertEqual(Fraction(-1, 0), Fraction(7, 8) - Fraction(4, 0))
        # 1/0 = 3/5 - (-2/0)
        self.assertEqual(Fraction(1, 0), Fraction(3, 5) - Fraction(-2, 0))
        # -1/0 = 7/0 - 2/7
        self.assertEqual(Fraction(1, 0), Fraction(7, 0) - Fraction(2, 7))
        # 1/0 = -3/0 - (-1/4)
        self.assertEqual(Fraction(-1, 0), Fraction(-3, 0) - Fraction(-1, 4))
        # 0/0(ValueError) = 1/0 - 8/0
        with self.assertRaises(ValueError):
            Fraction(1, 0) + Fraction(8, 0)
    
    def test_mul(self):
        self.assertEqual(Fraction(3,16), Fraction(1, 2) * Fraction(3, 8))

    def test_eq(self):
        f = Fraction(1, 2)
        g = Fraction(-40, -80)
        h = Fraction(10000, 20001) # not quite 1/2
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        f = Fraction(-3, 4)
        g = Fraction(15, -20)
        h = Fraction(9000, -11999)
        self.assertTrue(f == g)
        self.assertFalse(f == h)
        f = Fraction(0, 10)
        g = Fraction(0, -1000)
        self.assertTrue(f == g)
        self.assertFalse(f == h)
        f = Fraction(10, 0)
        g = Fraction(100, 0)
        h = Fraction(-500, 0)
        i = Fraction(-1000, 0)
        self.assertTrue(f == g)
        self.assertFalse(f == h)
        self.assertTrue(h == i)
