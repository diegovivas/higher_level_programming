#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        if isinstance(width, int) is False:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if isinstance(height, int) is False:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("width must be > 0")
        if isinstance(x, int) is False:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if isinstance(y, int) is False:
            raise TypeError("y must be an integer")
        if y < 0:
                raise ValueError("width must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__height = value

    @property
    def x(self):
        return x

    @x.setter
    def x(self, value):
        if isinstance(value, int) is False:
            raise TypeError("x must be an integer")
        if value < 0:
                raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return y

    @y.setter
    def y(self, value):
        if isinstance(value, int) is False:
            raise TypeError("y must be an integer")
        if value < 0:
                raise ValueError("width must be >= 0")
        self.__y = y

    def area(self):
        return (self.__width * self.__height)

    def display(self):
        print("\n" * self.__y, end="")
        for ojo in range(self.__height):
            print(" " * self.__x, end="")
            print("#"*self.__width)

    def __str__(self):
        palabra = "[Rectangle]"
        palabra += " ({})".format(self.id)
        palabra += " {}/".format(self.__x)
        palabra += "{} ".format(self.__y)
        palabra += "- {}".format(self.__width)
        palabra += "/{}".format(self.__height)
        return palabra

    def update(self, *args):
        argu = len(args)
        if argu >= 1:
            self.id = args[0]
        if argu >= 2:
            self.__width = args[1]
        if argu >= 3:
            self.__height = args[2]
        if argu >= 4:
            self.__x = args[3]
        if argu >= 5:
            self.__y = args[4]
