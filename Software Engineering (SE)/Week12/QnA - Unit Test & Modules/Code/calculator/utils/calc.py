import numpy as np

class Calc:
    def __init__(self):
        pass

    def add(self, a: int, b: int) -> int:
        return np.add(a, b)

    def mult(self, a: int, b: int) -> int:
        return np.multiply(a, b)

    def div(self, a: int, b: int) -> int:
        if b == 0:
            raise ZeroDivisionError("Division by 0")
        return a / b

    def sub(self, a: int, b: int) -> int:
        return np.subtract(a , b)