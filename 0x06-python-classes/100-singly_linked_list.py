#!/usr/bin/python3
"""Node Class
Node class for a signly linked list
"""


class Node:
    """Node Class
    This is the node class attributes and methods
    """

    def __init__(self, data, next_node=None):
        """__init__ method
        initializes node with data and next node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None:
            return value
        elif type(value) is not Node:
            raise TypeError("next_node must be a Node object")


"""SinglyLinkedList Class
the Class for a singly linked list (sorted one)
"""


class SinglyLinkedList:
    """SinglyLinkedList Class
    class for SLL which includes sorted_insert() method and the print() method
    """

    def __str__(self):
        """__str__ method
        adds printability to the class
        """
        my_str = ""
        current = self.__head

        while current:
            my_str += str(current.data)
            if current.__next_node is not None:
                my_str += "\n"
            current = current.__next_node

        return my_str

    def __init__(self):
        """__init__ method
        initializes head of SLL with none
        """
        self.__head = None

    def sorted_insert(self, value):
        """sorted_insert method
                inserts node in ascending order
                """
        newNode = Node(value)
        if self.__head is None:
            newNode.__next_node = self.__head
            self.__head = newNode
        elif self.__head.data >= newNode.data:
            newNode.__next_node = self.__head
            self.__head = newNode
        else:
            current = self.__head
            while(current.__next_node is not None and
                    current.__next_node.data < newNode.data):
                current = current.__next_node
            newNode.__next_node = current.__next_node
            current.__next_node = newNode
