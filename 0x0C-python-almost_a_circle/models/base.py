#!/usr/bin/python3
"""Base module
This module defines the base class for Rectangle and Square
"""
import json
import csv
from os import path


class Base:
    """Base class
    this is the class for the Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ method
        this method initializes on instance creation
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = f"{cls.__name__}.json"
        my_list = []

        for elem in list_objs:
            my_list.append(elem.to_dictionary())

        with open(filename, "w", encoding="utf-8") as my_file:
            my_file.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(3, 3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = f"{cls.__name__}.json"
        my_objects = []
        if not path.exists(filename):
            return my_objects
        with open(filename, mode="r", encoding="utf-8") as my_file:
            my_list = cls.from_json_string(my_file.read())
            for elem in my_list:
                my_objects.append(cls.create(**elem))
        return my_objects

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = f"{cls.__name__}.csv"
        my_list = []
        new_list = []
        for elem in list_objs:
            my_dict = elem.to_dictionary()
            for value in my_dict.values():

                new_list.append(value)
            my_list.append(new_list[:])
            new_list = []

        with open(filename, "w", encoding="utf-8") as my_file:
            writer = csv.writer(my_file)
            writer.writerows(my_list)

    @classmethod
    def load_from_file_csv(cls):
        filename = f"{cls.__name__}.csv"
        my_objects = []
        my_attr_rectangle = ["id", "width", "height", "x", "y"]
        my_attr_square = ["id", "size", "x", "y"]

        if not path.exists(filename):
            return my_objects

        with open(filename, mode="r", encoding="utf-8") as my_file:
            csv_reader = csv.reader(my_file)
            for line in csv_reader:

                if cls.__name__ == "Rectangle":
                    my_dict = {}
                    for i in range(len(line)):
                        my_dict[my_attr_rectangle[i]] = int(line[i])
                    my_objects.append(cls.create(**my_dict))

                if cls.__name__ == "Square":
                    my_dict = {}
                    for j in range(len(line)):
                        my_dict[my_attr_square[j]] = int(line[j])
                    my_objects.append(cls.create(**my_dict))

        return my_objects
