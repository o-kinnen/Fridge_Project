from expiration_date import ExpirationDate


class Food(ExpirationDate):
    """Class representing the food.

    Author : Anthony IV.
    Date : December 2022.
    This class allows the student to encode the information of food.
    """

    def __init__(self, libelle: str, food_type: str, nutriscore: str, origin: str,
                 caloric: int, nutritional_values: dict, expiration_date: str):
        """This build the food by libelle, food_type, nutriscore, origin, caloric, nutritional_values and
        expiration_date.

                PRE : - Object type string : libelle, food_type, nutriscore, origin and expiration_date.
                      - Object type int : caloric.
                      - Object type dict : students, nutritional_values.
                POST : - A object type string.
                RAISE: - SyntaxError if libelle is not a string.
                       - SyntaxError if food_type is not a string.
                       - SyntaxError if nutriscore is not a string.
                       - SyntaxError if origin is not a string.
                       - SyntaxError if caloric is not an integer.
                       - SyntaxError if nutritional_values is not a dictionary.
        """

        self.__libelle = libelle
        self.__food_type = food_type
        self.__nutriscore = nutriscore
        self.__origin = origin
        self.__caloric = caloric
        self.__nutritional_values = nutritional_values
        ExpirationDate.__init__(self, expiration_date)

    def get_lib(self):
        return self.__libelle

    def get_type(self):
        """Returns a representation of the type of food.
                PRE : /
                POST : - If string in type_food_list : string that represents the type of food.
                       - If not : string error that tells the student to choose the right type of food.
        """

        type_food_list = ["FRUIT", "VEGETABLE", "DAIRY PRODUCT", "MEAT", "FISH", "DRINK", "FAT", "SWEET PRODUCT",
                          "SALT"]
        if self.__food_type.upper() in type_food_list:
            return f"Type of food : {self.__food_type}."
        else:
            return "ERROR : Choose between fruit, vegetable, dairy product, meat, fish, drink, fat, sweet product or " \
                   "salt. "

    def get_nutriscore(self):
        """Returns a representation of the food's nutriscore.
                PRE : /
                POST : - If string in nutriscore_list : string that represents the nutriscore of the food.
                       - If not : string error that tells the student to choose a valid nutriscore.
        """

        nutriscore_list = ["A", "B", "C", "D", "E"]
        if self.__nutriscore.upper() in nutriscore_list:
            return f"Nutriscore : {self.__nutriscore}."
        else:
            return "ERROR : Choose between A, B, C, D or E."

    def get_origin(self):
        """Returns a representation of the origin of the food.
                PRE : /
                POST : - String that represents the origin of the food.
        """

        return f"The origin of the food : {self.__origin}."

    def get_caloric(self):
        """Returns a caloric representation of the food.
                PRE : /
                POST : - String that represents the caloric content of the food.
        """

        if self.__caloric < 0:
            return "ERROR, please enter a positive value."
        else:
            return f"Caloric value of the food : {self.__caloric}."

    def get_nutritional_values(self):
        """Returns a representation of the nutritional values of the food.
                PRE : /
                POST : - Dictionary representing the nutritional values of the food.
        """

        for i in self.__nutritional_values:
            if self.__nutritional_values[i] < 0:
                return "ERROR."
        return f"Nutritional value {self.__nutritional_values}"

    def __str__(self):
        """Return a textual representation of the food.
               PRE : /
               POST : String that represents the information of the food.
        """

        return f"Information about the food : \n\n" \
               f"Name of the food : {self.get_lib()}\n" \
               f"{self.get_type()}\n" \
               f"{self.get_nutriscore()}\n" \
               f"{self.get_origin()}\n" \
               f"{self.get_caloric()}\n" \
               f"{self.get_nutritional_values()}\n" \
               f"Expire on {self.expiration_date} and {self.time_count()} day(s) left."
