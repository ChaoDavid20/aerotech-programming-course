class Coordinate:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return float(self._x)

    @property
    def y(self):
        return float(self._y)

    @x.setter
    def x(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("The value must be a 'float' or 'int' type.")

        self._x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("The value must be a 'float' or 'int' type.")

        self._y = value

    def distance_to_origin(self):
        return ((self._x)**2 + (self._y)**2) ** 0.5

    def __add__(self, value2):
        return Coordinate(self._x + value2._x, self._y + value2._y)

    def __sub__(self, value2):
        return Coordinate(self._x - value2._x, self._y - value2._y)
