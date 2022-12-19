from food import Food


class Fridge(Food):
    """Class representing the Fridge

        Author : Anthony IV
        Date : December 2022
        This class allows the student to check the contents of the fridge
        """

    def __init__(self, students: dict, libelle: str, food_type: str, nutriscore: str, origin: str, caloric: int, nutritional_values: dict, expiration_date: str):
        """This builds a food's fridge by some students, libelle, food_type, nutriscore, origin, nutritional_values and expiration_date

                PRE : - Object type string : libelle, food_type, nutriscore, origin and expiration_date
                      - Object type int : caloric
                      - Object type dict : students, nutritional_values
                POST : /
                """
        self.content = {}
        self.students = students
        super().__init__(libelle, food_type, nutriscore, origin, caloric, nutritional_values, expiration_date)

    def check_inside(self):
        """Look at the contents of the fridge

                PRE : /
                POST : - String that represents the contents of the fridge
                """
        if self.content == {}:
            return f"The fridge is currently empty"
        else:
            return f"There are {self.content} in the fridge currently."

    def get_students(self):
        """Return a textual representation of the students

                PRE : /
                POST : - String that represents students who share the same fridge
                """
        if self.students == {}:
            return f"There are zero students"
        else:
            return f"The students who share the fridge are {self.students}."
