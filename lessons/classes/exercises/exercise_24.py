class Coordinate:
    """Coordinate class.

    This class represents the coordinates (x, y) of a given point.

    Attributes:_
        x: the x coordinate of a point.
        y: the y coordinate of a point.

    """

    def __init__(self, x, y):
        """Initialize a Coordinate instance.

        Args:_
            x: the x coordinate of the instance.
            y: the y coordinate of the instance.

        """
        self._x = x
        self._y = y

    @property
    def x(self):
        """Get the x coordinate of the instance.

        Returns_
            float(self._x): the x coordinate of the instance.

        """
        return float(self._x)

    @property
    def y(self):
        """Get the y coordinate of the instance.

        Returns_
            float(self._y): the y coordinate of the instance.

        """
        return float(self._y)

    @x.setter
    def x(self, value):
        """Set the x coordinate of the instance.

        Args:_
            value: the x coordinate of the instance.

        """
        if not isinstance(value, (float, int)):
            raise TypeError("The value must be a 'float' or 'int' type.")

        self._x = value

    @y.setter
    def y(self, value):
        """Set the y coordinate of the instance.

        Args:_
            value: the y coordinate of the instance.

        """
        if not isinstance(value, (float, int)):
            raise TypeError("The value must be a 'float' or 'int' type.")

        self._y = value

    def distance_to_origin(self):
        """Calculate the distance to origin of the instance.

        Returns_
            ((self._x)**2 + (self._y)**2) ** 0.5): the distance to origin of
                                                   the instance.

        """
        return ((self._x)**2 + (self._y)**2) ** 0.5

    def __add__(self, value2):
        """Add a coordinate instance to another.

        Args:_
            value2: the instance to be added.

        Returns_
            Coordinate(self._x + value2._x, self._y + value2._y): the result of
                                                                  the addition.

        """
        return Coordinate(self._x + value2._x, self._y + value2._y)

    def __sub__(self, value2):
        """Substract a coordinate instance from another.

        Args:_
            value2: the instance to be substracted.

        Returns_
            Coordinate(self._x - value2._x, self._y - value2._y): the result of
                                                                  the
                                                                  substraction.

        """
        return Coordinate(self._x - value2._x, self._y - value2._y)
