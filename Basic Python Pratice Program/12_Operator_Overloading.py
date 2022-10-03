class operator_overload:
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1

    def __str__(self):
        return f'({self.x1},{self.y1})'

    def __add__(self, operator):
        if not isinstance(operator, operator_overload):
            raise ValueError('The other must be an instance of the operator_overload')

        return operator_overload(self.x1 + operator.x1, self.y1 + operator.y1)

    def __sub__(self, other):
        if not isinstance(other, operator_overload):
            raise ValueError('The other must be an instance of the operator_overload')

        return operator_overload(self.x1 - other.x1, self.y1 - other.y1)


if __name__ == '__main__':
    a = operator_overload(20, 50)
    b = operator_overload(15, 35)
    c = b - a
    print(c)
