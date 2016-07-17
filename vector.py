from math import acos, sqrt, pi
from decimal import Decimal, getcontext







class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(c) for c in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __iter__(self):
        self.current = 0
        return self


    def __len__(self):
        return len(self.coordinates)

    def __getitem__(self, i):
        return self.coordinates[i]

    def __str__(self):
        return 'Vector: {}'.format([round(coord, 3)
                                    for coord in self.coordinates])

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def is_zero(self):
        return set(self.coordinates) == set([Decimal(0)])

    def plus(self, other):
        return Vector(map(sum, zip(self.coordinates, other.coordinates)))

    def minus(self, other):
        return Vector([coords[0] - coords[1]
                       for coords in zip(self.coordinates, other.coordinates)])

    def times_scalar(self, factor):
        return Vector([Decimal(factor) * coord for coord in self.coordinates])

    def magnitude(self):
        return Decimal(sqrt(sum([coord * coord
                                 for coord in self.coordinates])))

    def normalize(self):
        try:
            return self.times_scalar(Decimal('1.0') / self.magnitude())
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')



if __name__ == '__main__':

    v = Vector([-0.221, 7.437])
    first_magintude = v.magnitude()
    print 'first_magintude: {}'.format(round(first_magintude, 3))

    v = Vector([8.813, -1.331, -6.247])
    second_magintude = v.magnitude()
    print 'second_magintude: {}'.format(round(second_magintude, 3))

    v = Vector([5.581, -2.136])
    first_normalization = v.normalize()
    print 'first_normailization: {}'.format(first_normalization)

    v = Vector([1.996, 3.108, -4.554])
    second_normalization = v.normalize()
    print 'second_normailization: {}'.format(second_normalization)

