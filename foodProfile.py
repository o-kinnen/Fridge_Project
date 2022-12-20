from students import Student


class FoodProfile(Student):
    """Class representing the food profile of a student.

    Author : Arthur Kalinowska
    Date : Décembre 2022
    This class allows a student to create and check his food profile.
    """

    def __init__(self, firstname: str, lastname: str, diet: str,
                 allergy: str, gender: str, age: int, weight: int, height: int):
        """This builds a student's food profile by some firstname, lastname, diet, allergy,
        gender, age, weight and height.

        PRE : - Object type string : firstname, lastname, diet, allergy, gender
              - Object type int : age, weight, height
        POST : /
        """

        self.diet = diet
        self.__allergy = allergy
        super().__init__(lastname, firstname, gender, age, height, weight)

    def get_diet(self):
        """Return a representation of the diet of the student.

        PRE : /
        POST : - if string in diet_list : string which represents the diet of the student.
               - if not : string error which tells the student to choose the right diet.
        """
        diet_list = ["CARNIVOROUS", "OMNIVOROUS", "VEGETARIAN", "VEGETALIAN", "VEGAN"]
        if self.diet.upper() in diet_list:
            return self.diet
        else:
            return "ERROR : CHOOSE BETWEEN CARNIVOROUS, OMNIVOROUS, VEGETARIAN, VEGETALIAN OR VEGAN"

    def allergy(self):
        return self.__allergy

    def imc(self):
        """Return a representation of the calories a student have to eat every day to be in a good form.

        PRE : /
        POST : Integer which represents the daily needed calories of the student.
        """
        if self.get_weight() < 0 or self.get_height() < 0:
            return -1
        else:
            imc = self.get_weight() / ((self.get_height() / 100) ** 2)
            return round(imc, 1)

    def imc_details(self):
        """Return a representation of the details of the imc of a student.

        PRE : /
        POST : String which represents the details of the imc of the student.
        """
        imc_details = "Maybe there is a problem."

        if 14.5 <= self.imc() <= 18.5:
            imc_details = "Underweight"
        if 18.5 < self.imc() <= 25:
            imc_details = "Normal"
        if 25 < self.imc() <= 30:
            imc_details = "Overweight"
        if 30 < self.imc() <= 35:
            imc_details = "Obese"
        if self.imc() > 35:
            imc_details = "Extremely obese"

        return imc_details

    def daily_needed_calories(self):
        """Return a representation of the calories a student have to eat every day to be in a good form.

        PRE : /
        POST : Integer which represents the daily needed calories of the student.
        """

        if self.get_sex() == "F":
            dnc = (10 * self.get_weight()) + (6.25 * self.get_height()) - (5 * self.get_age()) - 161
            return int(dnc)
        if self.get_sex() == "M":
            dnc = (10 * self.get_weight()) + (6.25 * self.get_height()) - (5 * self.get_age()) + 5
            return int(dnc)
        else:
            return "ERROR : PLEASE WRITE A RIGHT GENDER !"

    # ------------------ Displays Profile ------------------

    def __str__(self):
        """Return a textual representation of the food profile

        PRE : /
        POST : String which represents the food profile of the student
        """

        profile = f"Food profile of the student : \n\n" \
                  f"{self.get_student()}"\
                  f"Diet : {self.get_diet()}\n" \
                  f"Allergy : {self.__allergy}\n" \
                  f"IMC : {self.imc()}\n" \
                  f"Details : {self.imc_details()}\n"\
                  f"Daily Needed Calories : {self.daily_needed_calories()}\n"

        return profile
