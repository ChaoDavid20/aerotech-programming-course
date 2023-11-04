class Car:
    """Car class.

    This class represents a car with 3 attributes (color, license plate and
    vin number).

    Attributes:_
        color: the color of the car.
        license plate: the license plate of the car.
        vin number: the vin number of the car.

    """

    def __init__(self, color, license_plate, vin_number):
        """Initialize a Car instance.

        Args:_
            color: the color of the instance.
            license_plate: the license plate of the instance.
            vin_number: the vin number of the instance.

        """
        self.color = color
        self._license_plate = license_plate
        self.__vin_number = vin_number


my_car = Car("red", "1234ABCD", 12340987)
ext_color = my_car.color
ext_license_plate = my_car._license_plate
ext_vin_number = my_car._Car__vin_number
