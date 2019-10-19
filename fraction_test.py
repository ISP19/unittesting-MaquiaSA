import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_init(self):
        with self.assertRaises(TypeError):
            Fraction(0.1, 8)
        with self.assertRaises(TypeError):
            Fraction(12, 1.3)
        with self.assertRaises(TypeError):
            Fraction('a', 4)
        with self.assertRaises(TypeError):
            Fraction(18, 'b')
        with self.assertRaises(TypeError):
            Fraction(True, 4)
        with self.assertRaises(TypeError):
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
        f = Fraction(0, 0)
        self.assertEqual("0/0", f.__str__())

    def test_add(self):
        # 3/4 == 2/3 + 1/12
        self.assertEqual(Fraction(3, 4), Fraction(1, 12) + Fraction(2, 3))
        # 1/2 == 6/8 + (-1/4)
        self.assertEqual(Fraction(1, 2), Fraction(6, 8) + Fraction(-1, 4))
        # -4/5 == (-1/10) + (-3/10) + (-2/5)
        self.assertEqual(Fraction(-4, 5), Fraction(-1, 10) + Fraction(-3, 10) + Fraction(-2, 5))
        # 1/3 == 2/6 + 0/5
        self.assertEqual(Fraction(1, 3), Fraction(2, 6) + Fraction(0, 5))
        # 1/0 == -7/8 + 4/0 (inf == -7/8 + inf)
        self.assertEqual(Fraction(1, 0), Fraction(-7, 8) + Fraction(4, 0))
        # -1/0 == 3/5 + (-2/0) (-inf == 3/5 + (-inf))
        self.assertEqual(Fraction(-1, 0), Fraction(3, 5) + Fraction(-2, 0))
        # 0/0 == 1/0 + (-1/0) (NaN = inf + (-inf))
        self.assertEqual(Fraction(0, 0), Fraction(1, 0) + Fraction(-1, 0))
    
    def test_sub(self):
        # 1/5 == 1 - 4/5
        self.assertEqual(Fraction(1, 5), Fraction(1) - Fraction(4, 5))
        # -1 == -2/3 - 7/8
        self.assertEqual(Fraction(-1), Fraction(-2, 3) - Fraction(7, 8) - Fraction(-13, 24))
        # 9/8 == 5/8 - (-1/2)
        self.assertEqual(Fraction(9, 8), Fraction(5, 8) - Fraction(-1, 2))
        # 3/4 == 3/4 - 0
        self.assertEqual(Fraction(-3, 4), Fraction(0) - Fraction(3, 4))
        # -3/4 == 0 - 3/4
        self.assertEqual(Fraction(-3, 4), Fraction(0) - Fraction(3, 4))
        # 2/7 == 2/7 - 0/3
        self.assertEqual(Fraction(2, 7), Fraction(2, 7) - Fraction(0, 3))
        # 0 == 0/2 - 0/6
        self.assertEqual(Fraction(0), Fraction(0, 2) - Fraction(0, 6))
        # -1/0 == 7/8 - 4/0 (-inf = 7/8 - inf)
        self.assertEqual(Fraction(-1, 0), Fraction(7, 8) - Fraction(4, 0))
        # 1/0 == 3/5 - (-2/0) (inf = 3/5 - (-inf))
        self.assertEqual(Fraction(1, 0), Fraction(3, 5) - Fraction(-2, 0))
        # 1/0 == 7/0 - 2/7 (inf = inf - 2/7)
        self.assertEqual(Fraction(1, 0), Fraction(7, 0) - Fraction(2, 7))
        # -1/0 == -3/0 - (-1/4) (-inf = -inf - (-1/4))
        self.assertEqual(Fraction(-1, 0), Fraction(-3, 0) - Fraction(-1, 4))
        # 0/0 == 1/0 - 1/0 (Nan = inf - inf)
        self.assertEqual(Fraction(0, 0), Fraction(1, 0) - Fraction(1, 0))
    
    def test_mul(self):
        # 3/16 == 1/2 * 3/8
        self.assertEqual(Fraction(3, 16), Fraction(1, 2) * Fraction(3, 8))
        # -1/2 == -1/4 * 2
        self.assertEqual(Fraction(-1, 2), Fraction(1, -4) * Fraction(2))
        # -7/5 == 4/5 * -7/4
        self.assertEqual(Fraction(-7, 5), Fraction(4, 5) * Fraction(-7, 4))
        # 6 == -1/4 * -24
        self.assertEqual(Fraction(6), Fraction(-1, 4) * Fraction(-24))
        # 0 == 0/5 * -1/4
        self.assertEqual(Fraction(0), Fraction(0, 5) * Fraction(-1, 4))
        # 1/0 == 2/0 * 3/4
        self.assertEqual(Fraction(1, 0), Fraction(2, 0) * Fraction(3, 4))
        # -1/0 == 1/7 * -3/0 (-inf = 1/7 * -inf)
        self.assertEqual(Fraction(-1, 0), Fraction(1, 7) * Fraction(-3, 0))
        # 1/0 == -2/3 * -1/0 (inf = -2/3 * -inf)
        self.assertEqual(Fraction(1, 0), Fraction(-2, 0) * Fraction(-1, 0))
        # 0/0 == 0 * -4/0 (NaN = 0 * -inf)
        self.assertEqual(Fraction(0, 0), Fraction(0) * Fraction(-4, 0))
        # 0/0 == 2/0 * 0 (NaN = inf * 0)
        self.assertEqual(Fraction(0, 0), Fraction(2, 0) * Fraction(0))
    
    def test_gt(self):
        # 2/7 > 8/29
        self.assertTrue(Fraction(2, 7) > Fraction(8, 29))
        # -3/6 > -4/10
        self.assertTrue(Fraction(-3, 6) > Fraction(4, -7))
        # -7/-21 > 8/27
        self.assertTrue(Fraction(-7, -21) > Fraction(1, 4))
        # 4/2 == 2
        self.assertFalse(Fraction(4, 2) > Fraction(2, 1))
        # 0/7 == 0/4
        self.assertFalse(Fraction(0, 7) > Fraction(0, 4))
        # 199/200 < 199/199
        self.assertFalse(Fraction(199, 200) > Fraction(199, 199))
        # -99/100 < -98/100
        self.assertFalse(Fraction(-99, 100) > Fraction(-98, 100))
        # 1/0 > 110000 (inf > 110000)
        self.assertTrue(Fraction(1, 0)> Fraction(110000))
        # 1/10000 > -200/0 (1/10000 > -inf)
        self.assertTrue(Fraction(1, 10000) > Fraction(-200, 0))
        # 0/0 != -1/0 (NaN != -inf)
        self.assertFalse(Fraction(0, 0) > Fraction(-1, 0))
        # 0/0 != 1/0 (NaN != inf)
        self.assertFalse(Fraction(0, 0) > Fraction(1, 0))
        # 0/0 != 0/0 (NaN != NaN)
        self.assertFalse(Fraction(0, 0) > Fraction(0, 0))
    
    def test_neg(self):
        # -(4/25) == -4/25
        self.assertEqual(Fraction(-4, 25), Fraction(4, 25).__neg__())
        # -(-2/17) == 2/17
        self.assertEqual(Fraction(2, 17), Fraction(-2, 17).__neg__())
        # -(-11/-13) == -11/13
        self.assertEqual(Fraction(-11, 13), Fraction(-11, -13).__neg__())
        # -(3/-8) == -3/-8 == 3/8
        self.assertEqual(Fraction(-3, -8), Fraction(3, -8).__neg__())
        # -(1/0) == -1/0
        self.assertEqual(Fraction(-1, 0), Fraction(1, 0).__neg__())
        # -(-2/0) == 2/0 == 1/0
        self.assertEqual(Fraction(2, 0), Fraction(-2, 0).__neg__())
        # -(0/10) == 0/10 == 0
        self.assertEqual(Fraction(0, 10), Fraction(0, 10).__neg__())
        # -(0/0) == 0/0 == 0/0
        self.assertEqual(Fraction(0, 0), Fraction(0, 0).__neg__())

    def test_eq(self):
        f = Fraction(1, 2)
        g = Fraction(-40, -80)
        h = Fraction(10000, 20001) # not quite 1/2
        # 1/2 == -40/-80
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        # 1/2 == 10000/20001
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        f = Fraction(-3, 4)
        g = Fraction(15, -20)
        h = Fraction(9000, -11999) # not quite -3/4
        # -3/4 == -15/20
        self.assertTrue(f == g)
        # -3/4 != -9000/11999
        self.assertFalse(f == h)
        f = Fraction(0, 10)
        g = Fraction(0, -1000)
        # 0/10 == -0/1000
        self.assertTrue(f == g)
        f = Fraction(10, 0)
        g = Fraction(100, 0)
        h = Fraction(-500, 0)
        i = Fraction(-1000, 0)
        # 0/10 == -0/1000 == 0
        self.assertTrue(f == g)
        # 0/10 != -0/1000
        self.assertFalse(f == h)
        # -500/0 == -1000/0 == -1/0
        self.assertTrue(h == i)

if __name__ == "__main__":
    unittest.main(verbosity=2)