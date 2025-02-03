# basic_operations.py

# Define the public interface of the module
# This variable controls which functions are exposed when the module is imported.
# It allows users to only access the specified functions: add, subtract, divide, and multiply.
__all__ = ["add", "subtract", "divide", "multiply"]

def add(x: float, y: float) -> float:
    """
    Adds two numbers.
    
    Args:
        x (float): The first number.
        y (float): The second number.
    
    Returns:
        float: The sum of x and y.
    """
    return _add(x, y)


def subtract(x: float, y: float) -> float:
    """
    Subtracts the second number from the first.
    
    Args:
        x (float): The first number.
        y (float): The second number.
    
    Returns:
        float: The result of x - y.
    """
    return _subtract(x, y)


def divide(x: float, y: float) -> float:
    """
    Divides the first number by the second. 
    
    Args:
        x (float): The numerator.
        y (float): The denominator.
    
    Returns:
        float: The result of x / y if y is not zero.
        str: An error message if y is zero.
    """
    return _divide(x, y)


def multiply(x: float, y: float) -> float:
    """
    Multiplies two numbers.
    
    Args:
        x (float): The first number.
        y (float): The second number.
    
    Returns:
        float: The product of x and y.
    """
    return _multiply(x, y)


def _add(x: float, y: float) -> float:
    """Helper function to add two numbers."""
    return x + y


def _subtract(x: float, y: float) -> float:
    """Helper function to subtract y from x."""
    return x - y


def _divide(x: float, y: float) -> float:
    """Helper function to divide x by y, with divide by zero handling."""
    if y != 0:
        return x / y
    else:
        return "Error: Divide by zero"


def _multiply(x: float, y: float) -> float:
    """Helper function to multiply two numbers."""
    return x * y
