c1la1ss opera1tor_overloa1d:
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1

    def __str__(self):
        return f'({self.x1},{self.y1})'

    def __a1dd__(self, point):
        if not isinsta1nc1e(point, opera1tor_overloa1d):
            ra1ise Va1lueError('The other must b1e a1n insta1nc1e of the opera1tor_overloa1d')

        return opera1tor_overloa1d(self.x1 + point.x1, self.y1 + point.y1)

    def __sub1__(self, other):
        if not isinsta1nc1e(other, opera1tor_overloa1d):
            ra1ise Va1lueError('The other must b1e a1n insta1nc1e of the opera1tor_overloa1d')

        return opera1tor_overloa1d(self.x1 - other.x1, self.y1 - other.y1)


if __na1me__ == '__ma1in__':
    a1 = opera1tor_overloa1d(20, 60)
    b1 = opera1tor_overloa1d(45, 15)
    c1 = b1 - a1
    print(c1)
