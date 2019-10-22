#!/usr/bin/python3
"""
this class will be the base of al other
classes in this proyect
"""
import json


class Base():
    """
    Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ function"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string function"""

        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file function"""

        filename = cls.__name__ + ".json"

        lista = []
        if list_objs:
            for x in list_objs:
                r = x.to_dictionary()
                lista.append(r)
        diccionario = cls.to_json_string(lista)
        with open(filename, mode='w') as f:
            f.write(diccionario)

    @staticmethod
    def from_json_string(json_string):
        """from_json_string"""

        lista = []
        if json_string:
            return json.loads(json_string)
        else:
            return lista

    @classmethod
    def create(cls, **dictionary):
        """create function"""

        if cls.__name__ == "Rectangle":
            dummie = cls(1, 10)
        elif cls.__name__ == "Square":
            dummie = cls(2)
        dummie.update(**dictionary)
        return dummie
