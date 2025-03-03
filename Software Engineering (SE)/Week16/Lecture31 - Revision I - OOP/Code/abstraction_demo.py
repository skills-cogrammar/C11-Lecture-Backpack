""" ****** Abstraction ****** """

# Importing ABC (Abstract Base Class) and abstractmethod
from abc import ABC, abstractmethod
# ABC - is a base class for defining abstract base classes.
# abstractmethod - is a decorator indicating that the method
#                  is abstract and must be implemented by any subclass

"""
An abstract base class (ABC) is a class that:

Subclasses can inherit from
- It defines a common interface and enforces method implementation in subclasses.
Cannot be instantiated
- You cannot create an object directly from an abstract base class
because it contains at least one abstract method that must be
implemented in a subclass.
"""


# Creating an Abstract Base Class
# The Shape class is defined as an abstract base class by inheriting from ABC.
class Shape(ABC):
    @abstractmethod             # decorator
    def area(self):
        """The area method is decorated with @abstractmethod,
           making it mandatory for subclasses to implement this method."""
        pass


# Demonstrating that Shape cannot be instantiated
try:
    shape = Shape()  # This will raise an error
except TypeError as e:
    print(f"Error: {e}")


class Rectangle(Shape):
    """The Rectangle class inherits from the abstract base class Shape."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """ The Rectangle class provides an implementation
            for the abstract area method. """
        return self.length * self.width


class Circle(Shape):
    """The Circle class inherits from the abstract base class Shape."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """ The Circle class provides an implementation
            for the abstract area method. """
        return 3.14 * self.radius ** 2


# Usage
rect = Rectangle(5, 4)
print(f"Rectangle Area: {rect.area()}")  # Output: 20

circle = Circle(3)
print(f"Circle Area: {circle.area()}")  # Output: 28.26
