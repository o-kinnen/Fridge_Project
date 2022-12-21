from foodProfile import *
from fridge import *
from recipe import *
import argparse

parser = argparse.ArgumentParser = argparse.ArgumentParser(
    description="Simulation of a virtual fridge for students living in a kot.")
args = parser.parse_args()

if __name__ == "__main__":
    fridge = []
    student = []
    recipes = []
    ingredients = {}
    food_profiles = []
    while True:
        print("1. Encode your food profile.\n2. View Food Profiles.\n3. See the fridge.\n4. Add foods.\n5. Remove "
              "foods.\n6. Encode a recipe.\n7. History of recipes.\n8. Quit.")

        choice = input("What do you want to do? (type the number): ")

        if choice == "1":
            lastname = input("Enter your name: ")
            firstname = input("Enter your first name: ")
            weight = int(input("Enter your weight: "))
            height = int(input("Enter your height (in cm): "))
            age = int(input("Enter your age: "))
            gender = input("Enter your gender (F or M): ")
            diet = input("Enter your diet (carnivorous, omnivorous, vegetarian, vegan): ")
            allergy = input("Enter your possible allergies: ")

            food_profile = FoodProfile(firstname, lastname, diet, gender, age, weight, height, allergy)
            food_profiles.append(food_profile)
            print(food_profile)

        elif choice == "2":
            if not food_profiles:
                print("No food profile was encoded.")
            else:
                for profile in food_profiles:
                    print(profile)

        elif choice == "3":
            if not fridge:
                print("The fridge is empty.")
            else:
                for food in fridge:
                    print(food)

        elif choice == "4":
            libelle = input("Enter the name of the food: ")
            food_type = input("Enter the type of food (fruit or vegetable or dairy product or meat or"
                              " fish or drink or fat or sweet product or salt): ")
            nutriscore = input("Enter the nutriscore of the food (A or B or C or D or E): ")
            origin = input("Enter the origin of the food: ")
            caloric = int(input("Enter the calorie count of the food: "))
            expiration_date = input("Enter the expiry date (AAAA-MM-DD): ")

            nutritional_values = {}
            name_nutritional = ["protein", "lipid", "carbohydrate", "fiber"]
            for name in name_nutritional:
                values = int(input("Enter Nutrition Facts " + name + " of the food: "))
                nutritional_values[name] = values

            food = Food(libelle, food_type, nutriscore, origin, caloric, nutritional_values, expiration_date)
            print(food)
            fridge.append(food)

        elif choice == "5":
            print("In Progress")
            pass

        elif choice == "6":
            response_libelle = "yes"
            response_ingredient = "yes"
            libelle = input("Enter the recipe name: ")
            while response_ingredient.lower() == "yes":
                ingredient_name = input("Enter the name of the ingredient: ")
                ingredient_qty = int(input("Enter the required quantity: "))
                ingredients[ingredient_name] = ingredient_qty
                response_ingredient = input("Do you want to add an ingredient? "
                                            "(if yes: enter yes/if no: press another key) ")
            while response_libelle.lower() == "yes":
                student_name = input("Enter the name of the student who can make the recipe: ")
                student.append(student_name)
                response_libelle = input("Do you want to add a student? "
                                         "(if yes: type yes/if no: press another key) ")
            recipe = Recipe(libelle, ingredients, student)
            recipes.append(recipe)
            print(recipe)

        elif choice == "7":
            if not recipes:
                print("No recipes have yet been encoded.")
            else:
                for recipe in recipes:
                    print(recipe)
        elif choice == "8":
            print("Thank you for using our program !")
            break
        else:
            print("Choose a number between 1 and 8")
