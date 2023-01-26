import utility


class Point:
    def __init__(self, x1, y1, z1):
        self.x = x1
        self.y = y1
        self.z = z1

    def __eq__(self, other):
        x = utility.epsilon_equal(self.x, other.x)
        y = utility.epsilon_equal(self.y, other.y)
        z = utility.epsilon_equal(self.z, other.z)
        return x and y and z


class Vector:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        x1 = utility.epsilon_equal(self.x, other.x)
        y1 = utility.epsilon_equal(self.y, other.y)
        z1 = utility.epsilon_equal(self.z, other.z)
        return x1 and y1 and z1


class Ray:
    def __init__(self, pt, dir):
        self.pt = pt
        self.dir = dir

    def __eq__(self, other):
        pt1 = Point.__eq__(self.pt, other.pt)
        dir1 = Vector.__eq__(self.dir, other.dir)
        return pt1 and dir1


class Sphere:
    def __init__(self, center, radius, color, finish):
        self.center = center
        self.radius = radius
        self.color = color
        self.finish = finish

    def __eq__(self, other):
        center1 = Point.__eq__(self.center, other.center)
        radius1 = utility.epsilon_equal(self.radius, other.radius)
        color1 = Color.__eq__(self.color, other.color)
        finish1 = Finish.__eq__(self.finish, other.finish)
        return center1 and radius1 and color1 and finish1


class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __eq__(self, other):
        r1 = utility.epsilon_equal(self.r, other.r)
        g1 = utility.epsilon_equal(self.g, other.g)
        b1 = utility.epsilon_equal(self.b, other.b)
        return r1 and g1 and b1


class Finish:
    def __init__(self, ambient, diffuse, specular, roughness):
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.roughness = roughness

    def __eq__(self, other):
        ambient_return = utility.epsilon_equal(self.ambient, other.ambient)
        diffuse_return = utility.epsilon_equal(self.diffuse, other.diffuse)
        specular_return = utility.epsilon_equal(self.specular, other.specular)
        roughness_return = utility.epsilon_equal(self.roughness, other.roughness)
        return ambient_return and diffuse_return and specular_return and roughness_return


class Light:
    def __init__(self, pt, color):
        self.pt = pt
        self.color = color

    def __eq__(self, other):
        pt_equal = utility.epsilon_equal(self.pt, other.pt)
        color_equal = utility.epsilon_equal(self.color, other.color)
        return pt_equal and color_equal

