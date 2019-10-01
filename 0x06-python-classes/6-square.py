#!/usr/bin/python3
class Square:

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self._Square__size * self._Square__size)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (not isinstance(value[0], int) or not isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        i = 0
        if (self.size == 0):
            print()
        else:
            print("\n" * self.__position[1], end="")
            while (i < self.size):
                print(" " * self.__position[0], end="")
                print("#" * self.size)
                i += 1
