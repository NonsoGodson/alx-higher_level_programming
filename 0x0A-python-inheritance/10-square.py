#!/usr/bin/python3
"""Square Class"""


Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size):
        """Instantiation"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
