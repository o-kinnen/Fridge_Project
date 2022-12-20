class SyntaxError(Exception):
    print("Elément de type non adéquat.")


class EmptyError(Exception):
    print("Elément vide non autorisé.")


class Recipe:
    def __init__(self, libelle: str, ingredients: dict, student: list):
        """Initialise les recettes.

                PRE : /
                POST : Une nouvelle recette est créé.
                RAISES : - EmptyError si libelle vaut "".
                         - EmptyError si student est vide.
                         - EmptyError si ingredients est vide.
                         - SyntaxError si libelle n'est pas un string.
                         - SyntaxError si student n'est pas une liste.
                         - SyntaxError si ingredients n'est pas un dictionnaire.
                """
        if libelle == "" or ingredients == {} or student == []:
            raise EmptyError
        if type(libelle) != str or type(ingredients) != dict or type(student) != list:
            raise SyntaxError
        self.libelle = libelle
        self.ingredients = ingredients
        self.student = student

    def get_lib(self):
        return self.libelle

    def get_ing(self):
        return self.ingredients

    def student(self):
        return self.student

    def check_inside(self, food: str):
        """Vérifie si un aliment spécifique est nécessaire à la recette.

                PRE : /
                POST : Un object de type str.
                RAISES : - EmptyError si food vaut "".
                         - SyntaxError si food n'est pas de type str.
                """
        if food == "":
            raise EmptyError
        if type(food) != str:
            raise SyntaxError
        if food in self.ingredients:
            response = f"L'aliment {food} est bien l'un des ingrédients de la recette {self.libelle}."
        else:
            response = f"L'aliment {food} n'est pas l'un des ingrédients de la recette {self.libelle}."
        return response
