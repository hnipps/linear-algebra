from math import *

class Vector(object):

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def add(self, vector_2):
        """
        Adds together the given vectors and returns the result as a new vector
        """
        new_coordinates = []
        index = 0
        while index < self.dimension:
            new_value = self.coordinates[index] + vector_2.coordinates[index]
            new_coordinates.append(new_value)
            index += 1
        new_vector = Vector(new_coordinates)
        return new_vector

    def subtract(self, vector_2):
        """
        Subtracts vector_2 from self and returns the result as a new vector
        """
        new_coordinates = []
        index = 0
        while index < self.dimension:
            new_value = self.coordinates[index] - vector_2.coordinates[index]
            new_coordinates.append(new_value)
            index += 1
        new_vector = Vector(new_coordinates)
        return new_vector

    def apply_scalar(self, scalar):
        """
        Applies a scalar to the given vector and returns the result as a new vector
        """
        new_coordinates = []
        index = 0
        while index < self.dimension:
            new_value = self.coordinates[index] * scalar
            new_coordinates.append(new_value)
            index += 1
        new_vector = Vector(new_coordinates)
        return new_vector
    

    def magnitude(self):
        """
        Calculates the magnitude of the vector
        """
        value_sum = 0
        for value in self.coordinates:
            value_sum += value ** 2
        magnitude = sqrt(value_sum)
        return magnitude


    def normalised(self):
        """
        Calculates the unit vector
        """
        try:
            inverse_magnitude = 1 / self.magnitude()
            unit_vector = self.apply_scalar(inverse_magnitude)
            return unit_vector
        except ZeroDivisionError:
            raise Exception('Cannot normalise the zero vector')
    

    def dot(self, vector_2):
        """
        Calculates the dot product of this vector and another vector
        """
        dot_product = 0
        i = 0
        for value in self.coordinates:
            product = value * vector_2.coordinates[i]
            dot_product += product
            i += 1

        return dot_product
    

    def rad_angle(self, vector_2):
        """
        Finds the angle, in radians, between this vector and the given vector
        """
        dot_product = self.dot(vector_2)
        angle = acos(dot_product / (self.magnitude() * vector_2.magnitude()))
        if angle > pi:
            return 2 * pi - angle
        else:
            return angle
    

    def deg_angle(self, vector_2):
        """
        Finds the angle, in degrees, between this vector and the given vector
        """
        rad_angle = self.rad_angle(vector_2)
        return rad_angle * (180 / pi)
    

    def isParallelTo(self, vector_2):
        """
        Determines whether or not the vector is parallel to the given vector
        """
        if self.magnitude() == 0 or vector_2.magnitude() == 0:
            return True
        else:
            unit_vector_1 = self.normalised()
            unit_vector_2 = vector_2.normalised()
            coordinates_1 = unit_vector_1.absoluteCoordinates()
            coordinates_2 = unit_vector_2.absoluteCoordinates()
            coordinates_1 = self.roundCoordinates(coordinates_1, 12)
            coordinates_2 = self.roundCoordinates(coordinates_2, 12)
            return coordinates_1 == coordinates_2
    

    def isOrthogonalTo(self, vector_2):
        """
        Determines whether or not the vector is orthogonal to the given vector
        """
        dot = self.dot(vector_2)
        return abs(round(dot, 12)) == 0
    

    def absoluteCoordinates(self):
        """
        Returns the abolute value of the vectors coordinates
        """
        abs_coordinates = tuple()
        for coordinate in self.coordinates:
            abs_coordinates += (abs(coordinate),)
        return abs_coordinates
    

    def roundCoordinates(self, coordinates, precision):
        """
        Rounds te coordinates to the given precision
        """
        rounded_coordinates = tuple()
        for coordinate in coordinates:
            rounded_coordinates += (round(coordinate, precision),)
        return rounded_coordinates


def quiz_1():
    VECTOR_1 = Vector([8.218, -9.341])
    VECTOR_2 = Vector([-1.129, 2.111])

    VECTOR_3 = Vector([7.119, 8.215])
    VECTOR_4 = Vector([-8.223, 0.878])

    VECTOR_5 = Vector([1.671, -1.012, -0.318])
    SCALAR = 7.41

    print(VECTOR_1.add(VECTOR_2))
    print(VECTOR_3.subtract(VECTOR_4))
    print(VECTOR_5.apply_scalar(SCALAR))
    return


def quiz_2():
    vector_1 = Vector([-0.221, 7.437])
    vector_2 = Vector([8.813, -1.331, -6.247])

    vector_3 = Vector([5.581, -2.136])
    vector_4 = Vector([1.996, 3.108, -4.554])

    print(vector_1.magnitude())
    print(vector_2.magnitude())
    print(vector_3.normalised())
    print(vector_4.normalised())


def quiz_3():
    vector_1 = Vector([7.887, 4.138])
    vector_2 = Vector([-8.802, 6.776])
    
    vector_3 = Vector([-5.955, -4.904, -1.874])
    vector_4 = Vector([-4.496, -8.755, 7.103])

    vector_5 = Vector([3.183, -7.627])
    vector_6 = Vector([-2.668, 5.319])

    vector_7 = Vector([7.35, 0.221, 5.188])
    vector_8 = Vector([2.751, 8.259, 3.985])

    print(vector_1.dot(vector_2))
    print(vector_3.dot(vector_4))
    print(vector_6.rad_angle(vector_5))
    print(vector_7.deg_angle(vector_8))


def quiz_4():
    vector_1 = Vector([-7.579, -7.88])
    vector_2 = Vector([22.737, 23.64])
    print("V1 - V2")
    print(vector_1.isParallelTo(vector_2))
    print(vector_1.isOrthogonalTo(vector_2))

    vector_3 = Vector([-2.029, 9.97, 4.172])
    vector_4 = Vector([-9.231, -6.639, -7.245])
    print("V3 - V4")
    print(vector_3.isParallelTo(vector_4))
    print(vector_3.isOrthogonalTo(vector_4))

    vector_5 = Vector([-2.328, -7.284, -1.214])
    vector_6 = Vector([-1.821, 1.072, -2.94])
    print("V5 - V6")
    print(vector_5.isParallelTo(vector_6))
    print(vector_5.isOrthogonalTo(vector_6))

    vector_7 = Vector([2.118, 4.827])
    vector_8 = Vector([0, 0])
    print("V7 - V8")
    print(vector_7.isParallelTo(vector_8))
    print(vector_7.isOrthogonalTo(vector_8))


quiz_4()

