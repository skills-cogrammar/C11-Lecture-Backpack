# Laptop class with special methods __init__, __str__, and __repr__
class Laptop:
    def __init__(self, brand, serial_number, screen_size):
        self.brand = brand
        self.serial_number = serial_number
        self.screen_size = screen_size

    def __str__(self):
        # Custom string representation for print function
        str_rep = f"Brand: {self.brand}\nSerial: {self.serial_number}\n"
        str_rep += f"Screen Size: {self.screen_size}\n"
        return str_rep

    def __repr__(self):
        # Representation used by the repr() function and other contexts
        return f"Laptop({self.brand},{self.serial_number},{self.screen_size})"


# Creating an instance of Laptop
laptop = Laptop("Asus", "ASHDBHS", "17")
print(laptop)           # Using __str__
print(repr(laptop))     # Using __repr__


# ===========================================
# MyNumber class with special methods __init__, __str__, and __add__
class MyNumber:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        # Custom string representation for print function
        return str(self.value)

    def __add__(self, other):
        # Custom addition operation
        return MyNumber(self.value + other.value)


# Creating instances of MyNumber and performing addition
num1 = MyNumber(25)
num2 = MyNumber(14)
num3 = num1 + num2  # Uses the __add__ method
print(num1)
print(num2)
print(num3)


# =============================
# Rectangle class with special methods __init__, get_area, __add__, and __sub__
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        """
        getter method that can be upgraded to
        read protected/private variables
        """
        return self.length * self.width

    def __add__(self, other):
        """ Custom addition operation for rectangles """
        length = self.length + other.length
        width = self.width + other.width
        return Rectangle(length, width)

    def __sub__(self, other):
        """ Custom subtraction operation for rectangles """
        length = self.length - other.length
        width = self.width - other.width
        return Rectangle(length, width)


# Creating instances of Rectangle and performing addition
rect1 = Rectangle(11, 6)
rect2 = Rectangle(7, 3)
rect3 = rect1 - rect2  # Uses the __sub__ method
print(rect3.get_area())

rect4 = rect1 + rect2  # Uses the __add__ method
print(rect4.get_area())


# ============================================
# ContactList as a container-like class and Contact class with 
# special methods __init__, __getitem__, __len__, and __contains__
class ContactList:
    def __init__(self):
        self.contact_list = []

    def add_contact(self, contact):
        self.contact_list.append(contact)

    def __getitem__(self, key):
        # Custom method to retrieve items by index
        return self.contact_list[key]

    def __len__(self):
        # Custom method to get the length of the contact list
        return len(self.contact_list)

    def __contains__(self, item):
        # Custom method to check if a contact is in the list
        for contact in self.contact_list:
            if contact.name == item:
                return True
        return False


class Contact:
    """ Add class docstring """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Contact: {self.name}"


# Creating instances of ContactList and Contact, and performing operations
contact_list = ContactList()
contact_list.add_contact(Contact("James"))  # Creating and adding instance
contact_list.add_contact(Contact("Joe"))

print(contact_list[1])              # Using __getitem__ & Contact.__str__
print(f"Number of contacts: {len(contact_list)}") # Using __len__

if "James" in contact_list:         # Using __contains__
    print("James is here.")


# =========================================
# Student class with special methods __init__, get_average, __gt__, and __ge__
class Student:
    """ Add class docstring """
    def __init__(self, fullname, student_number, grades) -> None:
        self.fullname = fullname
        self.student_number = student_number
        self.__grades = grades

    def get_average(self):
        """ Custom method to calculate the average of grades """
        return sum(self.__grades)/len(self.__grades)

    def __gt__(self, other):
        """ Custom greater than comparison based on average grades """
        return self.get_average() > other.get_average()

    def __ge__(self, other):
        """ Custom greater than or equal comparison based on average grades """
        return self.get_average() >= other.get_average()


# Creating instances of Student and performing comparisons
student1 = Student("Jack", "Jackson", [88, 68, 78, 78])
student2 = Student("John", "Johnson", [75, 78, 72, 88])

print(student1.__grades)  # Error: Avoid accessing private attribute directly

if student1 >= student2:        # Using __ge__
    print("Student 1 has the greater or equal average!")
else:
    print("Student 2 has the greater average!")


# ========== BONUS Special Method Example ===================
# Counter class with special methods __init__, __iter__, and __next__
class Counter:
    """ Add class docstring """
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = 0    # Code will work without this but with Pylint Err

    def __iter__(self):
        """ This method is called when an iterator object is requested """
        self.current = self.start
        return self

    def __next__(self):
        """ This method is called to get the next value in the iteration """
        if self.current < self.end:
            result = self.current
            self.current += 1
            return result
        else:
            # To signal the end of the iteration, raise StopIteration
            raise StopIteration


# Creating an instance of the Counter class
counter = Counter(1, 6)

# Make the instance iterable
iterator = iter(counter)

# Iterating using next()
print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
print(next(iterator))  # Output: 4
print(next(iterator))  # Output: 5

# Attempting to go beyond the end of the iteration
# try:
#     print(next(iterator))
# except StopIteration:
#     print("Iteration finished.")
