#!/usr/bin/python3


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        diict = {}
        hola = self.__dict__
        if type(attrs) == list:
            for at in attrs:
                try:
                    diict.setdefault(at, self.__dict__[at])
                except Exception:
                    pass
        else:
            return hola

        return diict

    def reload_from_json(self, json):
        pass
