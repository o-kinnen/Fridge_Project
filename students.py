class Student:
    """Class representing a student in a flat.

    Author : Arthur Kalinowska
    Date : Décembre 2022
    This class allows a student to encode everything we need to know to create a profile.
    """

    def __init__(self, lastname: str, firstname: str, gender: str, age: int, height: int, weight: int):
        """This builds a student's profile by some lastname, firstname, gender, age, height, weight.

        PRE : /
        POST : - object : type string
        """

        self.__lastname = lastname
        self.__firstname = firstname
        self.__weight = weight
        self.__height = height
        self.__age = age
        self.__gender = gender

    def get_lastname(self):
        """Return a textual representation of the lastname of the student.

        PRE : /
        POST : String which represents the lastname of the student.
        """
        if len(self.__firstname) == 0:
            return "SYNTAX ERROR : PLEASE WRITE A LASTNAME !"
        else:
            return self.__lastname

    def get_firstname(self):
        """Return a textual representation of the firstname of the student.

        PRE : /
        POST : String which represents the firstname of the student.
        """
        if len(self.__firstname) == 0:
            return "SYNTAX ERROR : PLEASE WRITE A FIRSTNAME !"
        else:
            return self.__firstname

    def get_weight(self):
        """Return a representation of the weight of the student.

        PRE : /
        POST : Int which represents the weight of the student.
        """
        if self.__weight <= 0:
            return -1
        else:
            return int(self.__weight)

    def get_height(self):
        """Return a representation of the height of the student.

        PRE : /
        POST : Integer which represents the height of the student.
        """
        if self.__height <= 0:
            return -1
        else:
            return int(self.__height)

    def get_age(self):
        """Return a representation of the age of the student.

        PRE : /
        POST : Integer which represents the age of the student
        """
        if self.__age <= 0:
            return -1
        if len(str(self.__age)) > 2:
            return -1
        else:
            return int(self.__age)

    def get_sex(self):
        """Return the textual representation of the gender of the student.

        PRE : /
        POST : String which represents the gender of the student.
        """
        if self.__gender == "M" or self.__gender == "F":
            return self.__gender
        else:
            return "SYNTAX ERROR, GENDER IS ONLY M OR F !!"

    # ------------------ Displays Student ------------------

    def get_student(self):
        """Return a textual representation of the student

        PRE : /
        POST : String which represents the profil of the student
        """

        student = f"Name : {self.__firstname} {self.__lastname}\n" \
                  f"Sex : {self.__gender}\n" \
                  f"Age : {self.__age}\n" \
                  f"Height : {self.__height}\n" \
                  f"Weight : {self.__weight}\n"

        return student
