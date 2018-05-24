from vector import Vector


def sum_vectors(vector_1, vector_2):
    """
    Adds together the given vectors and returns the result as a new vector
    """
    new_coordinates = []
    index = 0
    while index < vector_1.dimension:
        new_value = vector_1.coordinates[index] + vector_2.coordinates[index]
        new_coordinates.append(new_value)
        index += 1
    new_vector = Vector(new_coordinates)
    return new_vector


def subtract_vectors(vector_1, vector_2):
    """
    Subtracts vector_2 from vector_1 and returns the result as a new vector
    """
    new_coordinates = []
    index = 0
    while index < vector_1.dimension:
        new_value = vector_1.coordinates[index] - vector_2.coordinates[index]
        new_coordinates.append(new_value)
        index += 1
    new_vector = Vector(new_coordinates)
    return new_vector


def apply_scalar(vector, scalar):
    """
    Applies a scalar to the given vector and returns the result as a new vector
    """
    new_coordinates = []
    index = 0
    while index < vector.dimension:
        new_value = vector.coordinates[index] * scalar
        new_coordinates.append(new_value)
        index += 1
    new_vector = Vector(new_coordinates)
    return new_vector


VECTOR_1 = Vector([8.218, -9.341])
VECTOR_2 = Vector([-1.129, 2.111])

VECTOR_3 = Vector([7.119, 8.215])
VECTOR_4 = Vector([-8.223, 0.878])

VECTOR_5 = Vector([1.671, -1.012, -0.318])
SCALAR = 7.41

print(sum_vectors(VECTOR_1, VECTOR_2))
print(subtract_vectors(VECTOR_3, VECTOR_4))
print(apply_scalar(VECTOR_5, SCALAR))
