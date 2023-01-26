import unittest
import data
import vector_math
from collisions import *


class TestData(unittest.TestCase):
    def test_point(self):
        p = data.Point(2, 3, 4)
        self.assertEqual(p.x, 2)
        self.assertEqual(p.y, 3)
        self.assertEqual(p.z, 4)

    def test_vector(self):
        v = data.Vector(1.1, 3.3, 5.5)
        self.assertEqual(v.x, 1.1)
        self.assertEqual(v.y, 3.3)
        self.assertEqual(v.z, 5.5)

    def test_ray(self):
        r = data.Ray((1, 2), (1, 2, 3))
        self.assertEqual(r.pt, (1, 2))
        self.assertEqual(r.dir, (1, 2, 3))

    def test_sphere(self):
        s = data.Sphere((1, 2), 5.643)
        self.assertEqual(s.center, (1, 2))
        self.assertEqual(s.radius, 5.643)

    def test_scale(self):
        v = data.Vector(1, 2, 3)
        scale_vector = vector_math.scale_vector(v, 1.5)
        self.assertEqual(scale_vector.x, 1.5)
        self.assertEqual(scale_vector.y, 3)
        self.assertEqual(scale_vector.z, 4.5)

        v = data.Vector(2, 4, 6)
        scale_vector = vector_math.scale_vector(v, 1.5)
        self.assertEqual(scale_vector.x, 3)
        self.assertEqual(scale_vector.y, 6)
        self.assertEqual(scale_vector.z, 9)

    def test_dot_vec(self):
        vector1 = data.Vector(2, 4, 6)
        vector2 = data.Vector(1, 3, 5)
        self.assertEqual(vector_math.dot_vector(vector1, vector2), 44)

        vector1 = data.Vector(9, 12, 16)
        vector2 = data.Vector(1, 3, 5)
        self.assertEqual(vector_math.dot_vector(vector1, vector2), 125)

    def test_length(self):
        vector = data.Vector(10, 15, 20)
        self.assertAlmostEqual(vector_math.length_vector(vector), 26.9, 1)

        vector = data.Vector(5, 15, 30)
        self.assertAlmostEqual(vector_math.length_vector(vector), 33.9, 1)

    def test_normalize(self):
        vector = data.Vector(5, 12, 17)
        vector1 = vector_math.normalize_vector(vector)
        self.assertAlmostEqual(vector1.x, .23, 2)
        self.assertAlmostEqual(vector1.y, .56, 2)
        self.assertAlmostEqual(vector1.z, .79, 2)

        vector = data.Vector(3, 1, 2)
        vector1 = vector_math.normalize_vector(vector)
        self.assertAlmostEqual(vector1.x, .80, 2)
        self.assertAlmostEqual(vector1.y, .27, 2)
        self.assertAlmostEqual(vector1.z, .53, 2)

    def test_difference_pt(self):
        point1 = data.Point(2, 3, 4)
        point2 = data.Point(1, 2, 3)
        p = vector_math.difference_point(point1, point2)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 1)
        self.assertEqual(p.z, 1)

        point1 = data.Point(9, 12, 15)
        point2 = data.Point(1, 2, 3)
        p = vector_math.difference_point(point1, point2)
        self.assertEqual(p.x, 8)
        self.assertEqual(p.y, 10)
        self.assertEqual(p.z, 12)

    def test_difference_vector(self):
        vector1 = data.Vector(1.5, 2.5, 3.5)
        vector2 = data.Vector(0.5, 1.5, 2.5)
        vector = vector_math.difference_vector(vector1, vector2)
        self.assertEqual(vector.x, 1)
        self.assertEqual(vector.y, 1)
        self.assertEqual(vector.z, 1)

        vector1 = data.Vector(6.5, 8.5, 10.5)
        vector2 = data.Vector(0.5, 1.5, 2.5)
        vector = vector_math.difference_vector(vector1, vector2)
        self.assertEqual(vector.x, 6)
        self.assertEqual(vector.y, 7)
        self.assertEqual(vector.z, 8)

    def test_translate(self):
        point = data.Point(9, 0, 1)
        vector = data.Vector(1, 2, 3)
        p = vector_math.translate_point(point, vector)
        self.assertEqual(p.x, 10)
        self.assertEqual(p.y, 2)
        self.assertEqual(p.z, 4)

        point = data.Point(1, 2, 3)
        vector = data.Vector(1, 2, 3)
        p = vector_math.translate_point(point, vector)
        self.assertEqual(p.x, 2)
        self.assertEqual(p.y, 4)
        self.assertEqual(p.z, 6)

    def test_vector_from_to(self):
        to_point = data.Point(5, 6, 7)
        from_point = data.Point(1, 2, 3)
        vector = vector_math.vector_from_to(from_point, to_point)
        self.assertEqual(vector.x, 4)
        self.assertEqual(vector.y, 4)
        self.assertEqual(vector.z, 4)

        to_point = data.Point(9, 16, 20)
        from_point = data.Point(1, 2, 3)
        vector = vector_math.vector_from_to(from_point, to_point)
        self.assertEqual(vector.x, 8)
        self.assertEqual(vector.y, 14)
        self.assertEqual(vector.z, 17)



if __name__ == "__main__":
    unittest.main()
