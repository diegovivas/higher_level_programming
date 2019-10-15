#!/usr/bin/python3
class BaseGeometry:


    def __init__(self):
        self.area

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):


    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def print(self):
        print("[Rectangle] {}/{}".format(self.__width, self.__height))

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):


    def __init__(self, size):
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size

    def print(self):
        print("[Square] {}/{}".format(self.__size, self.__size))

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
