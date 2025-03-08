""" Add module docstring """


# ===========================  BATS    ===========================
# Using super() function for double inheritance of subclasses
class Animal:
    def __init__(self, species: str = "") -> None:
        self.species = species

    def make_sound(self):
        return f"The {self.species} makes a generic sound."


class Mammal(Animal):
    def __init__(self, fur_colour: str, species: str = "Mammal") -> None:
        super().__init__(species)
        self.fur_colour = fur_colour

    def show_colour(self):
        return f"The {self.species} is a {self.fur_colour} colour."

    def give_birth(self):
        return f"The {self.species} gives birth to live young."


class Bird(Animal):
    def __init__(self, beak_type: str, species: str = "Bird") -> None:
        super().__init__(species)
        self.beak_type = beak_type

    def eating(self):
        return f"The {self.species} is eating with its {self.beak_type} beak."


class Amphibian(Animal):
    def __init__(self, skin_type: str, species: str = "Amphibian", ) -> None:
        super().__init__(species)
        self.skin_type = skin_type

    def jump(self):
        return f"The {self.species} jumps with it's {self.skin_type} skin."


class Bat(Mammal, Bird):
    """ Add class docstring """
    def __init__(self, fur_colour: str, beak_type: str, species: str = "Bat") -> None:
        # Use explicit constructor calls of parent classes
        Mammal.__init__(self, fur_colour, species)
        Bird.__init__(self, beak_type, species)

        # Explicitly calls the constructors of both Mammal and Bird.
        # Each parent class constructor is called separately, ensuring
        # they both properly initialise their attributes.
        # This bypasses method resolution order (MRO) and
        # avoids diamond inheritance issues (if multiple inheritance exists).
        # -- Potential Issue:
        # If Mammal and Bird both inherit from the same base class,
        # this could call the base constructor multiple times,
        # causing redundant initialisation.

        # The below example however will not work as a result of MRO
        # Use super() to call constructors of parent classes
        # super().__init__(self, fur_colour, species)
        # self.beak_type = beak_type

    def echolocate(self):
        """ Add method docstring """
        return f"The {self.species} is using echolocation."


# ============ Main Code
# Create instances
mammal_instance = Mammal("golden", "Lion")        # fur_colour, species
bird_instance = Bird("hooked", "Eagle")           # beak_type, species
amphibian_instance = Amphibian("smooth", "Frog")  # skin_type, species
bat_instance = Bat("brown", "sharp", "Bat")   # fur_colour, beak_type, species

# Display information about animals
print(mammal_instance.make_sound())
print(mammal_instance.show_colour())
print(mammal_instance.give_birth())
print("===============")

print(bird_instance.make_sound())
print(bird_instance.eating())
print("===============")

print(amphibian_instance.make_sound())
print(amphibian_instance.jump())
print("===============")

print(bat_instance.make_sound())
print(bat_instance.echolocate())
print("===============")


# ========== BONUS Inheritance Example ===================
# Inheritance example for emotional support animals using an abstract method
# ==> The below is not a pure implementation of "Duck Typing" since subclasses
# are at least inheriting the name of the animal from the parent class.
class Animal:
    """ Add class docstring """
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        """ Add method docstring """
        raise NotImplementedError("Subclasses must implement the make_sound method")


class Dog(Animal):
    """ Add class docstring """
    def make_sound(self):
        return f"{self.name} barks: Woof, woof!"

    def fetch(self):
        """ Add method docstring """
        return f"{self.name} is fetching a ball."


class Cat(Animal):
    """ Add class docstring """
    def make_sound(self):
        return f"{self.name} meows: Meow, meow!"

    def climb_tree(self):
        """ Add metthod docstring """
        return f"{self.name} is climbing the tree."


class Bird(Animal):
    """ Add class docstring """
    def make_sound(self):
        return f"{self.name} chirps: Chirp, chirp!"

    def fly(self):
        """ Add method docstring """
        return f"{self.name} is flying."


class EmotionalSupportAnimal(Dog, Cat, Bird):
    """ Add class docstring """
    def __init__(self, name, support_task):
        # Call the constructors of all parent classes
        Dog.__init__(self, name)
        Cat.__init__(self, name)
        Bird.__init__(self, name)
        self.support_task = support_task

    def provide_support(self):
        """ Add method docstring """
        return f"{self.name} provides emotional support by {self.support_task}."


# Creating instances
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweetie")
esa_dog = EmotionalSupportAnimal("Rover", "being a loyal companion")

# Using methods from Dog
print(dog.make_sound())  # Output: Buddy barks: Woof, woof!
print(dog.fetch())       # Output: Buddy is fetching a ball.
print(f"{'-' * 30}")

# Using methods from Cat
print(cat.make_sound())    # Output: Whiskers meows: Meow, meow!
print(cat.climb_tree())    # Output: Whiskers is climbing the tree.
print(f"{'-' * 30}")

# Using methods from Bird
print(bird.make_sound())   # Output: Tweetie chirps: Chirp, chirp!
print(bird.fly())          # Output: Tweetie is flying.
print(f"{'-' * 30}")

# Using methods from EmotionalSupportAnimal
print(esa_dog.make_sound())     # Output: Rover barks: Woof, woof!
print(esa_dog.fetch())          # Output: Rover is fetching a ball.
print(esa_dog.climb_tree())     # Output: Rover is climbing the tree. (From Cat class)
print(esa_dog.provide_support())
