# Kod testujacy modul.

import unittest
from triangles import Triangle
from points import Point

class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.t1 = Triangle(1,2,1,3,2,2)

    def test_init_tri(self):
        with self.assertRaises(ValueError):
            Triangle(1,1,1,1)
        with self.assertRaises(ValueError):
            Triangle(1,1,1,2,1,3)

    def test_eq_tri(self):
        self.assertEqual(self.t1 == Triangle(1,2,1,3,2,2), True)
        self.assertEqual(self.t1 == Triangle(1,1,2,1,3,3), False)

    def test_center_tri(self):
        self.assertEqual(self.t1.center(), Point(1,2))
        self.assertNotEqual(self.t1.center(), Point(1,1))


    def test_area_tri(self):
        self.assertEqual(self.t1.area(), 0.5)
        self.assertNotEqual(self.t1.area(), 1.0)

    def test_move_tri(self):
        self.assertEqual(self.t1.move(99,99), Triangle(100,101, 100,102, 101,101))
        self.assertNotEqual(self.t1.move(99,99), Triangle(1,1,2,1,3,3))

    def test_make4_tri(self):
        self.assertEqual(self.t1.make4(), [Triangle(1, 2, 1.0, 2.5, 1.5, 2.0), Triangle(1.0, 2.5, 1, 3, 1.5, 2.5), Triangle(1.0, 2.5, 1.5, 2.0, 1.5, 2.5), Triangle(1.5, 2.0, 1.5, 2.5, 2, 2)])

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy