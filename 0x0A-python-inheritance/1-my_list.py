#!/usr/bin/python3
"""MyList Class
class for my list
"""


class MyList(list):
    """MyList class
    this class inherits from the list class
    """

    def print_sorted(self):
        print(sorted(self))


my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)
