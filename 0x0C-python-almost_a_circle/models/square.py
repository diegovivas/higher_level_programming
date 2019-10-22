#!/usr/bin/python3
"""
this class inherits from
 rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """__init__ function"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return super().width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """__str__ function"""
        palabra = "[Square]"
        palabra += " ({})".format(self.id)
        palabra += " {}/".format(self.x)
        palabra += "{} ".format(self.y)
        palabra += "- {}".format(self.width)
        return palabra

    def update(self, *args, **kwargs):
        """update function"""
        if args:
            argu = len(args)
            if argu >= 1:
                self.id = args[0]
            if argu >= 2:
                self.size = args[1]
            if argu >= 3:
                self.x = args[2]
            if argu >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key is 'size':
                    self.size = value
                if key is 'id':
                    self.id = value
                if key is 'x':
                    self.x = value
                if key is 'y':
                    self.y = value

    def to_dictionary(self):
        """to_dictionary function"""
        dictionary = {}
        dictionary.setdefault('id', self.id)
        dictionary.setdefault('size', self.size)
        dictionary.setdefault('x', self.x)
        dictionary.setdefault('y', self.y)
        return dictionary
