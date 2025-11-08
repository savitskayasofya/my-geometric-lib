import unittest
from rectangle import area, perimeter

class TestRectangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(3, 4), 12)
        with self.assertRaises(ValueError):
            area(-3, 4)

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4), 14)
        with self.assertRaises(ValueError):
            perimeter(3, -4)
