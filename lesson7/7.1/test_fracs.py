# Kod testujacy modul.

import unittest
from fracs import *

class TestFrac(unittest.TestCase):
    def setUp(self):
        self.f1 = Frac(1, 2)
        self.f2 = Frac(1, 4)
        self.f3 = Frac(3, 4)
        self.f4 = Frac(0, 1)
        self.f5 = Frac(1, 1)
        self.f6 = Frac(1, 4)
        self.f7 = Frac(-1, 4)

    def test_init_frac(self):
        with self.assertRaises(ValueError):
            Frac("ss","sss")

    def test_add_frac(self):
        self.assertEqual(self.f1+self.f2, self.f3)
        self.assertEqual(self.f1+self.f4, self.f1)
        self.assertEqual(self.f1 + 1, Frac(3,2))
        self.assertEqual(1 + self.f1, Frac(3, 2))
        with self.assertRaises(ValueError):
            self.f1 + "aaa"

    def test_sub_frac(self):
        self.assertEqual(self.f1 - self.f2, self.f6)
        self.assertEqual(self.f1 - self.f4, self.f1)
        self.assertEqual(self.f1 - 1, Frac(-1, 2))
        self.assertEqual(1 - self.f1, Frac(1, 2))

    def test_mul_frac(self):
        self.assertEqual(self.f1 * self.f2, Frac(1, 8))
        self.assertEqual(self.f1 * self.f5, self.f1)
        self.assertEqual(self.f1 * 2, 1)
        self.assertEqual(3 * self.f1,Frac(3,2))

    def test_div_frac(self):
        self.assertEqual(self.f1 / self.f2, Frac(2, 1))
        self.assertEqual(self.f1 / self.f5, self.f1)
        self.assertEqual(self.f1 / 2, Frac(1, 4))
        self.assertEqual(4 / self.f1, 8)

    def test_is_negative(self):
        self.assertEqual(-self.f1, Frac(-1,2))
        self.assertEqual(-self.f7, self.f6)

    def test_invert(self):
        self.assertEqual(~self.f1, Frac(2,1))
        self.assertEqual(~self.f7, Frac(4,-1))

    def test_cmp_frac(self):
        self.assertEqual(self.f1>self.f2, True)
        self.assertEqual(self.f1<self.f4, False)
        self.assertEqual(self.f1==Frac(2,4),True)
        self.assertEqual(self.f1 > 2, False)
        self.assertEqual(self.f1 < 3, True)
        self.assertEqual(4 == Frac(2, 4), False)

    def test_frac2float(self):
        self.assertEqual(float(self.f1), 0.5)
        self.assertEqual(float(self.f2), 0.25)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy