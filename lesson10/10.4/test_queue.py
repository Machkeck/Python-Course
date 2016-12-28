# Kod testujacy modul.

import unittest
from queue import *

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.q1 = Queue(3)
        self.q1.put(1)
        self.q1.put(2)
        self.q1.put(3)

        self.q2 = Queue(2)
        self.q2.put(1)
        self.q2.put(2)
        self.q2.get()
        self.q2.get()


    def test_put(self):
        with self.assertRaises(ValueError):
            self.q1.put(4)


    def test_get(self):
        with self.assertRaises(ValueError):
            self.q2.get()


    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy