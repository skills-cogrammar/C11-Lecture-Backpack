"""
This module defines the `Recipe` class, which represents a recipe with a name
and a list of ingredients.  It provides methods to display individual recipes,
list all recipes created, and convert ingredient measurements to grams.

Classes:
    - Recipe: Represents a recipe with methods for displaying details,
              listing all recipes, and converting measurements.

Methods:
    - disp_recipe(): Displays the name and ingredients
                     of a specific recipe instance.
    - disp_all_recipes(): Class method that lists all recipes created.
    - convert_to_g(amount, unit): Static method that converts ingredient
                                  measurements (spoons or cups) to grams.

Usage Example:
    ```python
    omelette = Recipe("Omelette", ["eggs", "cheese", "veggies"])
    omelette.disp_recipe()

    Recipe.all_recipes.append(omelette)
    Recipe.disp_all_recipes()

    grams = Recipe.convert_to_g(2, "spoons")
    print(f"2 spoons is {grams} grams")
    ```
"""


class Recipe:
    """
    A class to represent a recipe, tracking its name and ingredients.

    This class provides functionality to display individual recipes,
    maintain a list of all created recipes, and convert ingredient
    measurements to grams.

    Attributes:
        all_recipes (list): A class-level list storing 
        all instances of `Recipe`.

    Methods:
        __init__(name, ingredients):
            Initializes a new recipe with a name and list of ingredients.

        disp_recipe():
            Displays the recipe name and its ingredients.

        disp_all_recipes():
            Class method that lists all recipes created.

        convert_to_g(amount, unit):
            Static method that converts measurements (spoons or cups) to grams.
    """

    # `all_recipes` keeps track of all instances of Recipe created.
    all_recipes = []

    def __init__(self, name, ingredients):
        """
        Instance method that initialises the attributes `name` and
        `ingredients` for each instance of the Recipe class.

        :param name: Name of the recipe.
        :param ingredients: A list of ingredients used in the recipe.
        """
        self.name = name
        self.ingredients = ingredients

    def disp_recipe(self):
        """
        Instance method to display the details of the recipe. It prints the
        recipe name and its list of ingredients. This method operates on the
        instance level, meaning it shows the details of the specific recipe
        object it's called on.
        """
        print(f"Recipe: {self.name}")
        print("Ingredients")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")

    @classmethod
    def disp_all_recipes(cls):
        """
        Class method to display the names of all recipes created. This method
        operates at the class level, accessing the `all_recipes` class variable
        to list all recipes without the need to reference specific instances.
        """
        print("All Recipes")
        for recipe in cls.all_recipes:
            print(recipe.name)

    @staticmethod
    def convert_to_g(amount, unit):
        """
        Static method to convert measurements to grams. This method does not
        depend on the class or instance, as it operates independently of any
        specific Recipe object. 
        It converts units like spoons and cups into grams.

        :param amount: The quantity to be converted.
        :param unit: The unit of measurement ('spoons' or 'cups').
        :return: Equivalent amount in grams.
        """
        if unit == "spoons":
            return amount * 20
        if unit == "cups":
            return amount * 236

        return "Invalid unit"


# Create instances of Recipe
omelette_du_fromage = Recipe("Omelette", ["eggs", "cheese", "veggies"])
# Call the instance method to display this recipe's details
omelette_du_fromage.disp_recipe()

home_style_omelette = Recipe("Ommu", ["eggs", "flavour", "love"])
# Call the instance method to display this recipe's details
home_style_omelette.disp_recipe()

# Add instances to the class-level list of all recipes
Recipe.all_recipes.append(omelette_du_fromage)
Recipe.all_recipes.append(home_style_omelette)

# We can also adjust the code to automatically add the recipe to the
# all_recipes list when the object is created.
# To achieve this, simply append the recipe to the all_recipes list inside
# the __init__ method and remove the append lines above.

# def __init__(self, name, ingredients):
#         self.name = name
#         self.ingredients = ingredients
#         # Automatically add the recipe to the all_recipes list when the object
#         # is created.
#         Recipe.all_recipes.append(self)


# Call the class method to display all recipes created so far
Recipe.disp_all_recipes()

print()
# Static method example to convert measurements (cups to grams in this case)
cups = Recipe.convert_to_g(2, "cups")
print(f"2 cups in grams is {cups} grams")
