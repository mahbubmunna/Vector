import operator


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be non empty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    def __add__(self, other):
        return tuple(map(operator.add, self.coordinates, other.coordinates))

    def __sub__(self, other):
        return tuple(map(operator.sub, self.coordinates, other.coordinates))

    def __mul__(self, other):
        return tuple(map(operator.mul, self.coordinates, other.coordinates))


if __name__ == '__main__':
    my_vector = Vector([2])
    my_vector1 = Vector([1, 2, -3])
    print(my_vector * my_vector1)
