# Kod testujacy modul.

import unittest
from stack import *

class TestStack(unittest.TestCase):
    def setUp(self):
        self.s1 = Stack(3)
        self.s1.push(1)
        self.s1.push(2)
        self.s1.push(3)

        self.s2 = Stack(2)
        self.s2.push(1)
        self.s2.push(2)
        self.s2.pop()
        self.s2.pop()


    def test_push(self):
        with self.assertRaises(ValueError):
            self.s1.push(4)


    def test_pop(self):
        with self.assertRaises(ValueError):
            self.s2.pop()


    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy