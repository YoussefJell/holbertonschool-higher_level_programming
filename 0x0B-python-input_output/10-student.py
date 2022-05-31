#!/usr/bin/python3
"""Student Class"""


class Student:
    """Student Class
    defines a student
    """

    def __init__(self, first_name, last_name, age):
        """__init__ method
        Instantiation with first_name, last_name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json
        returns the dictionary description with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an object
        THIS TIME WITH A FILTER!!
        """
        my_dict = dict()

        if type(attrs) is list:
            for elem in attrs:
                if type(elem) is not str:
                    return self.__dict__

                if elem in self.__dict__:
                    my_dict[elem] = self.__dict__[elem]

            return my_dict

        return self.__dict__
