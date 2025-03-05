# Special Methods
# ================= __init__ and adding string representation.
# NOTE: __init__ can also include setup arguments
import re


class Student:
    def __init__(self, name, surname, age, email) -> None:
        """Initialise the student with a name, surname, age, and email."""

        # Email validation using regex
        if not self.is_valid_email(email):
            raise ValueError(f"Invalid email address: {email}")

        self.name = name
        self.surname = surname
        self.age = age
        self.email = email

        # Simulate sending a welcome email upon successful registration
        self.send_welcome_email()

        print(f"✅ Student {self.name} {self.surname} has been successfully registered.")

    def __str__(self) -> str:
        """Return a user-friendly string representation."""
        return f"Fullname: {self.name} {self.surname}\nAge: {self.age}\nEmail: {self.email}"

    def __repr__(self):
        """Return a developer-friendly string representation."""
        # !r below is a format specifier that tells Python to use the repr()
        # representation of self.name instead of the default str()
        # NOTE: the quotes around name and surname in the output
        return f"Student({self.name!r}, {self.surname!r}, {self.age!r}, {self.email!r})"

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """Check if the given email address is valid."""
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(email_regex, email) is not None

    def send_welcome_email(self):
        """Simulate sending a welcome email."""
        print(f"📧 Sending welcome email to {self.email}...")


# Example usage
try:
    student1 = Student("Alice", "Smith", 20, "alice.smith@example.com")
    # Demonstrating __str__ output (for users)
    print(student1)
    # Output: Fullname: Alice Smith
    #         Age: 20
    #         Email: alice.smith@example.com

    student2 = Student("Bob", "Jones", 21, "invalid-email")  # Will raise error
except ValueError as e:
    print(f"⚠️ Error: {e}")

# Demonstrating __repr__ output (for developers)
print(repr(student1))  # Output: Student('Alice', 'Smith', 20)

# Adding student to a list (shows __repr__ in lists and not __str__)
students = [student1]
print(students)  # Output: [Student('Alice', 'Smith', 20)]


# ------- Dunder Methods
class Person:
    """
    A class called Person with a custom dunder method __call__.
    The __call__ method allows instances of the class to be called
    as if they were functions.
    """
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}!"

    def __call__(self, other_person=None):
        if other_person is None:
            return self.greet()
        return f"{self.name} says: Hi, {other_person.name}!"


# Creating instances of Person
alice = Person("Alice")
bob = Person("Bob")

# Using the greet method
print(alice.greet())    # Output: Hello, my name is Alice!
print(bob.greet())      # Output: Hello, my name is Bob!

# Using the __call__ method, allowing instances to be called like functions
print(alice())          # Output: Hello, my name is Alice!
# Below is same as print(alice.__call__(bob))
print(alice(bob))       # Output: Alice says: Hi, Bob!
print(bob(alice))       # Output: Bob says: Hi, Alice!


# ================= Operator Overloading
class Rectangle:
    # Consider function or method annotations (ie. length: float)
    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    """
    When defining methods like __add__, __sub__, or similar,
    self refers to the instance the method is called on,
    and other refers to the second object involved in the operation.
    """
    def __add__(self, other):
        new_length = self.length + other.length
        new_width = self.width + other.width
        return Rectangle(new_length, new_width)

    def __sub__(self, other):
        new_length = self.length - other.length
        if new_length < 0:
            new_length = 0
        new_width = self.width - other.width
        if new_width < 0:
            new_width = 0
        return Rectangle(new_length, new_width)

    def __str__(self) -> str:
        return f"Length: {self.length}\nWidth {self.width}"


"""
The implementation for the below, all works the same as __add__ and __sub__
__eq__(self, other):	Behaviour for equality (==)
__ne__(self, other):	Behaviour for inequality (!=)
__lt__(self, other):	Behaviour for less-than (<)
__le__(self, other):	Behaviour for less-than-or-equal (<=)
__gt__(self, other):	Behaviour for greater-than (>)
__ge__(self, other):	Behaviour for greater-than-or-equal (>=)
"""
# Demonstration
rect1 = Rectangle(5, 7)
rect2 = Rectangle(4, 9)

# Both the below addition code options will work
rect3 = rect1 + rect2
# rect3 = rect1.__add__(rect2)

print(rect3)

"""
For 3 rectangles ->
rect1 = Rectangle(5, 7)
rect2 = Rectangle(4, 9)
rect3 = Rectangle(3, 6)

rect4 = rect1 + rect2 + rect3
This will be the same as  ((rect1 + rect2) + rect3)
"""


# ================= Container-like behaviour.
class BookShelf:

    def __init__(self, shelf_num, shelf_genre) -> None:
        """Initialise the bookshelf with a number, genre,
        and an empty list of books."""
        self.shelf_num = shelf_num
        self.shelf_genre = shelf_genre
        self.books = []

    def __getitem__(self, key):
        """Allow books to be accessed by index, like shelf[0]."""
        return self.books[key]

    def __len__(self):
        """Return the number of books on the shelf using len(shelf)."""
        return len(self.books)

    def __contains__(self, item):
        """Check if a specific book is on the shelf using 'in' keyword."""
        return item in self.books

    def __repr__(self) -> str:
        """Return a string representation of the bookshelf for developers."""
        return f'''BookShelf(shelf_num={self.shelf_num!r},
            shelf_genre={self.shelf_genre!r}, books={self.books!r})'''


# Example usage
shelf = BookShelf(1, "Dystopian Fiction")

# Adding books directly to the list for simplicity
shelf.books.extend(["1984", "Brave New World", "Fahrenheit 451"])

# Accessing books using __getitem__
print(shelf[0])  # Output: 1984

# Checking the number of books using __len__
print(len(shelf))  # Output: 3

# Checking if a book is on the shelf using __contains__
print("Brave New World" in shelf)  # Output: True

# Printing the current state of the bookshelf
print(shelf)  # Output: BookShelf(shelf_num=1, shelf_genre='Dystopian Fiction',
              # books=['1984', 'Brave New World', 'Fahrenheit 451'])

# ================= Polymorphism
# print() is an examples of polymorphism as it does not care about
# the type of object it is receiving.
print("Hello")
print(3.14)
print(100)
print(True)


# ================= Implementing polymorphism using method overloading.
class Calculator:
    def add(self, *args, **kwargs):
        """Adds numbers passed as positional or keyword arguments."""
        total = sum(args)  # Sum all positional arguments

        # Sum all keyword argument values if they are numbers
        total += sum(value for value in kwargs.values() if isinstance(value, (int, float)))
        # You can further deal with **kwargs like dictionaries
        # ie. for key, value in kwargs.items() - kwargs.keys. kwargs.values
        return total


# Example Usage
calc = Calculator()

print(calc.add(1, 2, 3))             # Output: 6
print(calc.add(10, 20, num=5))       # Output: 35
print(calc.add(a=2, b=3, c=4))       # Output: 9
print(calc.add(4, 5, x=10, y=15))    # Output: 34


# ================= Implementing polymorphism using method overriding.
# Let's go back to our animals and see what polymorphism means.
class Animal:
    def __init__(self, sound: str) -> None:
        """Initialise the animal with a sound it makes."""
        self.sound = sound

    def make_sound(self) -> str:
        """The default make_sound method for the Animal class."""
        return f"The animal makes a {self.sound} sound."


class Lion(Animal):
    def __init__(self) -> None:
        super().__init__("rawr")

    def make_sound(self) -> str:
        return f"The fierce lion let's out a big {self.sound}!!!!!!"


class Canary(Animal):
    def __init__(self) -> None:
        super().__init__("tweet")

    def make_sound(self) -> str:
        sound = "The canary tries to impress his partner with a song from the soul."
        sound += f"{self.sound} {self.sound} {self.sound}."
        return sound


class Goldfish(Animal):
    def __init__(self) -> None:
        super().__init__("blub")

    def make_sound(self) -> str:
        return f"{self.sound} {self.sound}...................  {self.sound}"


# Pay attention to the return values of all the make_sound() functions
# Let's create a function that will make use of this behaviour.
def sound(sound_object):
    print(sound_object.make_sound())


# With all our make_sound funtions returning the same value none of them
# will break our function when passed as an argument.
animals = [Lion(), Canary(), Goldfish()]
for animal in animals:
    sound(animal)


# What if we don't return the correct value type? No return in make_sound method
# NOTE: Remember to grab the Animal class and sound function from above.
class Dog(Animal):
    def __init__(self) -> None:
        super().__init__("woof")

    def make_sound(self) -> None:
        print(f"{self.sound} {self.sound} {self.sound}")


dog = Dog()
sound(dog)

# The above output "woof woof woof" comes from the print statement in make_sound 
# and since nothing was returned from the make_sound method, the sound function
# has nothing to print and therefor prints None


# ================= Duck typing
# If it walks like a duck, swims like a duck and quacks like a duck
# then it might just be a duck.
class Dog:
    def __init__(self, sound) -> None:
        self.sound = sound

    def make_sound(self) -> None:
        return f"{self.sound} {self.sound} {self.sound}"


class Student:
    def __init__(self, name, surname, age) -> None:
        self.name = name
        self.surname = surname
        self.age = age

    def make_sound(self):
        return f"Hi, I'm {self.name} {self.surname}. I am {self.age} years old!"


def sound(sound_object):
    print(sound_object.make_sound())


"""
Here, we define a Dog and a Student class with a method make_sound(), which
returns a string. The classes themselves are not explicitly tied to any other
class or interface, and it doesn't need to inherit from a specific base class
for the purpose of "making sound."

Duck Typing focuses on the presence of methods or properties, allowing objects
to be used interchangeably based on behaviour rather than class inheritance.

The function sound() can be used here for different objects and
different outcomes.
"""
student = Student("Jack", "Sparrow", 38)
sound(student)

dog = Dog("Woof")
sound(dog)
