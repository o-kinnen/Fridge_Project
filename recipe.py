class Recipe:
    """Class representing the recipe

            Author : Anthony IV
            Date : December 2022
            This class allows the student to receive a recipe
            """

    def __init__(self, libelle: str, ingredients: dict, student: list):
        """This class create a recipe

                PRE : /
                POST :- A object : type string
                RAISES: - SyntaxError if libelle is not a string
                        - SyntaxError if ingredients is not a dictionary
                        - EmptyError if ingredients is empty
                        - SyntaxError if student is not a list
                        - EmptyError if student is empty
                """
        self.libelle = libelle
        self.ingredients = ingredients
        self.student = student

    def get_lib(self):
        """Returns a textual representation of the recipe name

                PRE : /
                POST : String which represents the name of the recipe
        """
        return f"Name of the recipe : {self.libelle}"

    def get_ing(self):
        """Returns a textual representation with the ingredients needed for the recipe

                PRE : /
                POST : String that represents the ingredients of the recipe
        """
        return f"The ingredients needed for the recipe are : {self.ingredients}"

    def get_student(self):
        """Returns a list of students who can use the recipe according to their dietary profile

                PRE : /
                POST : - A object : type list
        """
        return self.student

    def check_inside(self, food: str):
        """Checks if a specific food is needed for the recipe.

                PRE : /
                POST : - A object : type string
                RAISES : SyntaxError if food is not of type str
                """
        if food in self.ingredients:
            response = f"The food {food} is indeed one of the ingredients of the recipe {self.libelle}"
        else:
            response = f"The food {food} is not one of the ingredients of the recipe {self.libelle}"
        return response
