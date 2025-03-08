"""
Below is how Python implements Method OverLoading with *args and **kwargs.
"""


class MathOperations:
    """ Add Class docstring """
    def add(self, *args):
        """ Add Method docstring """
        if len(args) >= 2:
            numbers = [num for num in args]
            result = sum(numbers)
            return result
        else:
            raise ValueError("Invalid number of arguments")


# Create an instance of the MathOperations class
math_instance = MathOperations()

# Call the add method with different numbers of arguments
result_2_params = math_instance.add(2, 3)          # Calls the add_two method
result_3_params = math_instance.add(2, 3, 4)       # Calls the add_three method

print(result_2_params)  # Output: 5
print(result_3_params)  # Output: 9
