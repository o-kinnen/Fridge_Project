from students import Student


class WeightError(Exception):
    pass


class HeightError(Exception):
    pass


class GenderError(Exception):
    pass


class AgeError(Exception):
    pass


class DietError(Exception):
    pass


class TypeError(Exception):
    pass


class ErrorName(Exception):
    pass


class FoodProfile(Student):
    """Class representing the food profile of a student.

    Author : Arthur Kalinowska
    Date : December 2022
    This class allows a student to create and check his food profile.
    """

    # à évaluer
    def __init__(self, firstname: str, lastname: str, diet: str,
                 gender: str, age: int, weight: int, height: int, allergy="Aucune"):
        """This builds a student's food profile by some firstname, lastname, diet, allergy,
        gender, age, weight and height.

        PRE : - Object type string : firstname, lastname, diet, allergy, gender
              - Object type int : age, weight, height
        POST : /
        """

        if type(allergy) != str:
            raise TypeError

        self.diet = diet
        self.__allergy = allergy

        super().__init__(lastname, firstname, gender, age, height, weight)

    # à évaluer
    def get_diet(self):
        """Return a representation of the diet of the student.

        PRE : /
        POST : - if string in diet_list : string which represents the diet of the student.
               - if not : string error which tells the student to choose the right diet.
        """
        if type(self.diet) != str:
            raise TypeError

        diet_list = ["CARNIVOROUS", "OMNIVOROUS", "VEGETARIAN", "VEGETALIAN", "VEGAN"]
        if self.diet.upper() in diet_list:
            return self.diet.lower()
        else:
            raise DietError

    def allergy(self):
        return self.__allergy

    # à évaluer
    def imc(self):
        """Return a representation of the calories a student have to eat every day to be in a good form.

        PRE : /
        POST : Integer which represents the daily needed calories of the student.
        """
        if type(self.get_weight()) != int:
            raise WeightError
        if type(self.get_height()) != int:
            raise HeightError
        if self.get_height() < 0:
            raise HeightError
        if self.get_weight() < 0:
            raise WeightError
        if self.get_height() > 300:
            raise HeightError
        if self.get_weight() > 300:
            raise WeightError

        imc = round(self.get_weight() / ((self.get_height() / 100) ** 2), 1)
        return imc

    # à évaluer
    def daily_needed_calories(self):
        """Return a representation of the calories a student have to eat every day to be in a good form.

        PRE : /
        POST : Integer which represents the daily needed calories of the student.
        """

        if type(self.get_weight()) != int:
            raise WeightError
        if type(self.get_height()) != int:
            raise HeightError
        if type(self.get_age()) != int:
            raise AgeError
        if self.get_height() < 0:
            raise HeightError
        if self.get_weight() < 0:
            raise WeightError
        if self.get_age() < 0:
            raise AgeError
        if self.get_height() > 300:
            raise HeightError
        if self.get_weight() > 300:
            raise WeightError
        if self.get_age() > 100:
            raise AgeError

        if self.get_sex() == "F":
            dnc = (10 * self.get_weight()) + (6.25 * self.get_height()) - (5 * self.get_age()) - 161
            return int(dnc)
        elif self.get_sex() == "M":
            dnc = (10 * self.get_weight()) + (6.25 * self.get_height()) - (5 * self.get_age()) + 5
            return int(dnc)
        else:
            raise GenderError

    # ------------------ Displays Profile ------------------

    # à évaluer
    def __str__(self):
        """Return a textual representation of the profile

        PRE : /
        POST : String which represents the full profile of the student
        """

        if type(self.get_firstname()) != str:
            raise ErrorName

        if type(self.get_lastname()) != str:
            raise ErrorName

        else:
            profile = f"Food profile of the student : \n\n" \
                  f"Name : {self.get_firstname()} {self.get_lastname()}\n" \
                  f"Sex : {self.get_sex()}\n" \
                  f"Age : {self.get_age()}\n" \
                  f"Height : {self.get_height()}\n" \
                  f"Weight : {self.get_weight()}\n" \
                  f"Diet : {self.get_diet()}\n" \
                  f"Allergy : {self.__allergy}\n" \
                  f"IMC : {self.imc()}\n" \
                  f"Daily Needed Calories : {self.daily_needed_calories()}\n"

        return profile
