#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize a square
        @size(int):size of the square
        @position(int, int) tuple postion of the square
        all validation done by the setter
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square's area"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                if i == 1:
                    print("\n" * self.__position[1], end="")
                print(" " * self.__position[0], end="")
                print("#" * self.__size)               
