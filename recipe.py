class TypeError(Exception):
    """Unsuitable type element."""
    pass


class EmptyError(Exception):
    """Empty element not allowed."""
    pass


class Recipe:
    """Class representing a recipe.

            Author : Olivia Kinnen.
            Date : December 2022.
            This class allows a student to encode a new recipe.
            """
    def __init__(self, libelle: str, ingredients: dict, student: list):
        """Initializes the recipes.

                PRE : /
                POST : A new recipe is created.
                RAISES : - EmptyError if libelle is "".
                         - EmptyError if student is empty.
                         - EmptyError if ingredients is empty.
                         - TypeError if libelle is not a string.
                         - TypeError if student is not a list.
                         - TypeError if ingredients is not a dictionary.
                """
        if libelle == "" or ingredients == {} or student == []:
            raise EmptyError
        if type(libelle) != str or type(ingredients) != dict or type(student) != list:
            raise TypeError
        self.libelle = libelle
        self.ingredients = ingredients
        self.student = student

    def get_lib(self):
        return self.libelle

    def get_ing(self):
        return self.ingredients

    def get_student(self):
        return self.student

    def check_inside(self, food: str):
        """Check if a specific food is needed for the recipe.

                PRE : /
                POST : An object of type str.
                RAISES : - EmptyError if food is "".
                         - TypeError if food is not a string.
                """
        if food == "":
            raise EmptyError
        if type(food) != str:
            raise TypeError
        if food in self.ingredients:
            response = f"The food {food} is one of the ingredients of the recipe {self.libelle}."
        else:
            response = f"The food {food} is not one of the ingredients of the recipe {self.libelle}."
        return response

    def __str__(self):
        return f"Information about the recipe {self.libelle} : \n\n" \
            f"Ingredients : {self.ingredients}\n" \
            f"Student(s) : {self.student}\n"
