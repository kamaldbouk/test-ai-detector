# This script was generated by an AI language model.
# It demonstrates a simple calculator class with basic operations.
# The code includes type hints, docstrings, and comments for clarity.

from typing import Union

Number = Union[int, float]

class Calculator:
    """
    A simple calculator class that can perform basic arithmetic operations.
    """

    def __init__(self):
        """
        Initialize the Calculator instance.
        """
        pass

    def add(self, a: Number, b: Number) -> Number:
        """
        Return the sum of two numbers.
        """
        return a + b

    def subtract(self, a: Number, b: Number) -> Number:
        """
        Return the difference between two numbers.
        """
        return a - b

    def multiply(self, a: Number, b: Number) -> Number:
        """
        Return the product of two numbers.
        """
        return a * b

    def divide(self, a: Number, b: Number) -> Number:
        """
        Return the division of two numbers.
        Raises a ZeroDivisionError if b is zero.
        """
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b


def main():
    """
    Demonstration of Calculator functionality.
    """
    calc = Calculator()
    print("Addition:", calc.add(10, 5))
    print("Subtraction:", calc.subtract(10, 5))
    print("Multiplication:", calc.multiply(10, 5))
    print("Division:", calc.divide(10, 5))


if __name__ == "__main__":
    main()
