import unittest
from sparsepolys import *

class TestSparsePolys(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]
        self.p1 = {10: 1, 0: 2}  # W(x) = x**10 + 2
        self.p2 = {100: 4, 5: 3}  # W(x) = 4 * x**100 + 3 * x**5
        self.p3 = {0: 3}  # W(x) = 3, wielomian zerowego stopnia
        self.p4 = {0: 0}  # zero
        self.p5 = {5: 0}  # zero (niejednoznaczność)

        self.p6 = {10: 2}
        self.p7 = {10: 1, 0: 2, 11: 2}

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1,self.p6), {0: 2, 10: 3})
        self.assertEqual(add_poly(self.p1,self.p2), {0: 2, 10: 1, 100:4, 5:3})

    def test_sub_poly(self):
        self.assertEqual(sub_poly(self.p1,self.p6), {0: 2, 10: -1})
        self.assertEqual(sub_poly(self.p1,self.p2), {0: 2, 10: 1, 100:-4, 5:-3})

    def test_mul_poly(self):
        self.assertEqual(mul_poly(self.p1,self.p2), {5: 6, 15: 3, 100:8, 110:4})

    def test_is_zero(self):
        self.assertEqual(is_zero(self.p3),False)
        self.assertEqual(is_zero(self.p4),True)

    def test_cmp_poly(self):
        self.assertEqual(cmp_poly(self.p1,self.p7),False)

    def test_eval_poly(self):
        self.assertEqual(eval_poly(self.p1,2),1026)

    def test_pow_poly(self):
        self.assertEqual(pow_poly(self.p1,3),{0: 8, 10: 12, 20: 6, 30: 1})

    def test_diff_poly(self):
        self.assertEqual(diff_poly(self.p7),{9: 10, 10: 22})

    def test_combine_poly(self):
        self.assertEqual(combine_poly({2:5,0:3},{1:6,2:2}),{0: 3, 2: 180, 3: 120, 4: 20})
        self.assertEqual(combine_poly({1:6,2:2},{2:5,0:3}), {0: 36, 2: 90, 4: 50})

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy