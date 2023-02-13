import unittest
from triangle import Triangle


class TestTriangleUnit(unittest.TestCase):

    def setUp(self):
        self.first = Triangle(9, 8, 7)

    def tearDown(self):
        del self.first

    def test_triangle_eq(self):
        second = Triangle(7, 8, 9)
        self.assertEqual(self.first, second)

    def test_triangle_perimetr(self):
        self.assertEqual(self.first.perimetr(), 24)

    def test_triangle_square(self):
        third = Triangle(3, 4, 5)
        self.assertEqual(third.square(), 6)

    def test_triangle_ne(self):
        second = Triangle(7, 10, 8)
        self.assertNotEqual(self.first, second)

    def test_triangle_lt(self):
        other = Triangle(10, 11, 12)
        self.assertLess(self.first, other)

    def test_triangle_gt(self):
        other = Triangle(5, 7, 8)
        self.assertGreater(self.first, other)

    def test_triangle_le(self):
        other = Triangle(10, 11, 12)
        self.assertLessEqual(self.first, other)

    def test_triangle_ge(self):
        other = Triangle(5, 7, 8)
        self.assertGreaterEqual(self.first, other)

    def test_triangle_equal_to_other(self):
        second = Triangle(18, 16, 14)
        self.assertTrue(self.first.equal(second))

    def test_triangle_is_right_angled(self):
        second = Triangle(3, 4, 5)
        self.assertTrue(second.is_right_angled())

    @unittest.skip('not sorted sides')
    def test_triangle_is_right_angled2(self):
        second = Triangle(5, 4, 3)
        self.assertTrue(second.is_right_angled())

    def test_triangle_is_right_triangle(self):
        third = Triangle(3, 3, 3)
        self.assertTrue(third.is_right_triangle())

    def test_triangle_two_sides_eq(self):
        second = Triangle(2, 3, 2)
        self.assertTrue(second.two_sides_eq())

    def test_triangle_del(self):
        second = Triangle(3, 4, 5)
        self.assertIsNone(second.__del__(), None)


if __name__ == '__main__':
    unittest.main()
