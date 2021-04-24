import math


class Vector(object):
    def __init__(self, *a):
        self.vec = list(a)

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter < len(self.vec):
            temp = self.counter
            self.counter += 1
            return self.vec[temp]
        else:
            raise StopIteration()

    def __getitem__(self, item):
        return self.vec[item]

    def __add__(self, other):
        return Vector(*((a + b) for a, b in zip(self.vec, other)))

    def __iadd__(self, other):
        for i in range(0, len(self.vec)):
            self.vec[i] += other[i]
        return self

    def __mul__(self, other):
        if type(other) is Vector:
            return sum((a * b) for a, b in zip(self.vec, other))
        else:
            return Vector(*((a * other) for a in self.vec))

    def __imul__(self, other):
        for i in range(0, len(self.vec)):
            self.vec[i] *= other
        return self

    def __eq__(self, other):
        return self.vec == other

    def __len__(self):
        return len(self.vec)

    def length(self):
        return math.sqrt(sum(a ** 2 for a in self.vec))

    def __str__(self):
        return str(self.vec)


vec_1 = Vector(1, 2.2, 3.3)

vec_2 = Vector(4, 5, 6)

vec_1 *= 9.2

print(vec_1)
