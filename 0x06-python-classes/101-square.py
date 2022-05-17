#!/usr/bin/python3
"""Square class

Defines a square class
and has private instance size

"""


class Square:
    """Square Class
    This square has a size an area a setter and a getter and
        a printer and finally a position :)
    """

    def __str__(self):
        my_str = ""
        k = 0
        if self.__size == 0:
            return my_str
        for i in range(self.__position[1]):
            my_str += "\n"
        for i in range(self.__size):
            for j in range(self.__size):
                while k < self.__position[0]:
                    my_str += " "
                    k += 1
                my_str += "#"
            k = 0
            if i is not (self.size - 1):
                my_str += "\n"
        return my_str

    def __init__(self, size=0, position=(0, 0)):
        """__init__
        initializing square
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int and type(position[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """area
        returns area of square
        """
        return self.__size * self.__size

    def my_print(self):
        """my_print
        prints the square
        """
        k = 0
        if self.__size == 0:
            print()
            return None
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                while k < self.__position[0]:
                    print(' ', end='')
                    k += 1
                print('#', end='')
            k = 0
            print()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int and type(value[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value


my_square = Square(5, (0, 0))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)
