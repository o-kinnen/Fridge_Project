class Recipe:
    def __init__(self, libelle: str, ingredients: dict, student: list):
        """Initialise les recettes.

                PRE : /
                POST : Une nouvelle recette est crée
                RAISES : - SyntaxError si libelle n'est pas un string
                         - SyntaxError si ingredients n'est pas un dictionnaire
                         - EmptyError si ingredients est vide
                         - SyntaxError si student n'est pas une liste
                         - EmptyError si student est vide
                """
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
                POST : Un object de type str
                RAISES : SyntaxError si food n'est pas de type str
                """
        if food in self.ingredients:
            response = f"L'aliment {food} est bien l'un des ingrédients de la recette {self.libelle}"
        else:
            response = f"L'aliment {food} n'est pas l'un des ingrédients de la recette {self.libelle}"
        return response
