# Kod testujacy modul.

import unittest
from times import *


class TestTime(unittest.TestCase):

    def setUp(self):
        self.t1 = Time(3600)
        self.t2 = Time(360)
        self.t3 = Time(60)
        self.t4 = Time(60)
        self.t5 = Time(3960)
        self.t6 = Time(0)

    def test_print(self):      # test str() i repr()
        self.assertEqual(self.t1.__str__(), "01:00:00")
        self.assertEqual(self.t6.__str__(), "00:00:00")
        self.assertEqual(self.t1.__repr__(), "Time(3600)")
        self.assertEqual(self.t6.__repr__(), "Time(0)")

    def test_add(self):
        self.assertEqual(Time(1) + Time(2), Time(3))
        self.assertEqual(self.t1 + self.t2, self.t5)
        self.assertNotEqual(self.t1 + self.t2, self.t3)
        self.assertEqual(self.t1 + self.t6, self.t1)

    def test_cmp(self):
        # Mozna sprawdzac ==, !=, >, >=, <, <=.
        self.assertTrue(Time(1) == Time(1))
        self.assertTrue(Time(1) != Time(2))
        self.assertTrue(Time(3) > Time(2))
        self.assertEqual(self.t1 >= self.t2, True)
        self.assertEqual(self.t3 > self.t4, False)
        self.assertEqual(self.t3 == self.t4, True)
        self.assertEqual(self.t4 <= self.t6, False)
        self.assertEqual(self.t4 < self.t3, False)
        self.assertEqual(self.t4 != self.t3, False)


    def test_int(self):
        self.assertEqual(int(self.t1), 3600)
        self.assertEqual(int(self.t2), 360)
        self.assertNotEqual(int(self.t3),"60")
        self.assertEqual(int(self.t3), float(60))

    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()     # wszystkie testy
