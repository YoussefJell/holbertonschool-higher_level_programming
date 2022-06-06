#!/usr/bin/python3
"""Rectangle module
This module defines a Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class
    this is the class for rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ method
        this method initializes on instance creation
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """__str__ method
        this method will print the rectangle on print() or str()
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -\
 {self.__width}/{self.__height}"

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.check_value_w_h(value, "width")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.check_value_w_h(value, "height")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.check_value_w_h(value, "x")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.check_value_w_h(value, "y")
        self.__y = value

    def check_value_w_h(self, value, name):
        """check_value_w_h method
        this method will check the value with a name
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value < 0 and name in ('x', 'y'):
            raise ValueError(f"{name} must be >= 0")
        if value <= 0 and name in ("height", "width"):
            raise ValueError(f"{name} must be > 0")

    def area(self):
        """area Method
        this method will calculate the rectangle object's area
        """
        return self.__height * self.__width

    def display(self):
        """display Method
        this method will display the rectangle
        """
        for space in range(self.__y):
            print("")
        for i in range(self.__height):
            for space in range(self.__x):
                print(" ", end='')
            for j in range(self.__width):
                print("#", end='')
            print("")

    def update(self, *args, **kwargs):
        """update Method
        this method will assign a key/value argument to attributes
        """
        argc = len(args)
        kwargc = len(kwargs)
        my_list = ["id", "width", "height", "x", "y"]
        if argc > 0:
            if argc > len(my_list):
                argc = len(my_list)
            for i in range(argc):
                setattr(self, my_list[i], args[i])
        elif kwargc > 0:
            for key, value in kwargs.items():
                if key in my_list:
                    setattr(self, key, value)

    def to_dictionary(self):
        """to_dictionary Method
        this method will return the dictionary representation of a Rectangle
        """
        return {"id": self.id, "width": self.width, "height":
                self.height, "x": self.x, "y": self.y}
