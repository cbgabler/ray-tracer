import math
import data


def sqr(x):
    return x * x


def scale_vector(vector, scalar):
    x = vector.x * scalar
    y = vector.y * scalar
    z = vector.z * scalar
    return data.Vector(x, y, z)


def dot_vector(vector1, vector2):
    vector_x = (vector1.x * vector2.x)
    vector_y = (vector1.y * vector2.y)
    vector_z = (vector1.z * vector2.z)
    answer_dot_vector = (vector_x + vector_y + vector_z)
    return answer_dot_vector


def length_vector(vector):
    def sqr(x):
        return x * x

    vector = math.sqrt((sqr(vector.x)) + (sqr(vector.y)) + (sqr(vector.z)))
    return vector


def normalize_vector(vector):
    length_vector = math.sqrt((sqr(vector.x)) + (sqr(vector.y)) + (sqr(vector.z)))
    x = (vector.x / length_vector)
    y = (vector.y / length_vector)
    z = (vector.z / length_vector)
    return data.Vector(x, y, z)


def difference_point(point1, point2):
    x = (point1.x - point2.x)
    y = (point1.y - point2.y)
    z = (point1.z - point2.z)
    return data.Vector(x, y, z)


def difference_vector(vector1, vector2):
    x = (vector1.x - vector2.x)
    y = (vector1.y - vector2.y)
    z = (vector1.z - vector2.z)
    return data.Vector(x, y, z)


def translate_point(point, vector):
    x = (point.x + vector.x)
    y = (point.y + vector.y)
    z = (point.z + vector.z)
    return data.Point(x, y, z)


def vector_from_to(from_point, to_point):
    x = (to_point.x - from_point.x)
    y = (to_point.y - from_point.y)
    z = (to_point.z - from_point.z)
    return data.Vector(x, y, z)

def calculate_distance(x1, x2, y1, y2):
    distance_calc = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance_calc