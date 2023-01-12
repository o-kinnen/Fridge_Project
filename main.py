import argparse

from fridge import *
from recipe import *
from foodProfile import *

from kivy.app import App
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

parser = argparse.ArgumentParser = argparse.ArgumentParser(
    description="Simulation of a virtual fridge for students living in a kot.")
args = parser.parse_args()


class ProfileApp(App):

    def build(self):
        self.title = "Food Profile of the student"
        profile_box = BoxLayout(orientation="vertical")

        # Informations du profil alimentaire encodé
        name_label = Label(text=f"Name : {food_profile.get_firstname()} {food_profile.get_lastname()}")
        sex_label = Label(text=f"Sex : {food_profile.get_sex()}")
        age_label = Label(text=f"Age : {food_profile.get_age()}")
        height_label = Label(text=f"Height : {food_profile.get_height()}")
        diet_label = Label(text=f"Diet : {food_profile.get_diet()}")
        allergy_label = Label(text=f"Allergy : {food_profile.allergy()}")
        imc_label = Label(text=f"IMC : {food_profile.imc()}")
        daily_needed_calories_label = Label(text=f"Daily Needed Calories : {food_profile.daily_needed_calories()}")

        # Ajout des infos dans la boîte profile_box
        profile_box.add_widget(name_label)
        profile_box.add_widget(sex_label)
        profile_box.add_widget(age_label)
        profile_box.add_widget(height_label)
        profile_box.add_widget(diet_label)
        profile_box.add_widget(allergy_label)
        profile_box.add_widget(imc_label)
        profile_box.add_widget(daily_needed_calories_label)

        return profile_box


class FoodApp(App):

    def build(self):
        self.title = "Information about the food"
        food_box = BoxLayout(orientation="vertical")

        # Informations de l'aliment encodé
        libelle_label = Label(text=food.get_lib())
        food_type_label = Label(text=food.get_type())
        nutriscore_label = Label(text=food.get_nutriscore())
        origin_label = Label(text=food.get_origin())
        caloric_label = Label(text=food.get_caloric())
        nutritional_values_label = Label(text=food.get_nutritional_values())
        expiration_date_label = Label(text=f"Expire on {food.expiration_date} and {food.time_count()} day(s) left.")

        # Ajout des infos dans la boîte profile_box
        food_box.add_widget(libelle_label)
        food_box.add_widget(food_type_label)
        food_box.add_widget(nutriscore_label)
        food_box.add_widget(origin_label)
        food_box.add_widget(caloric_label)
        food_box.add_widget(nutritional_values_label)
        food_box.add_widget(expiration_date_label)

        return food_box


class RecipeApp(App):
    def build(self):
        self.title = "Recipe"
        recipe_box = BoxLayout(orientation="vertical")

        # Informations de la recette encodée
        libelle_label = Label(text=f"Information about the recipe {recipe.get_lib()}")
        ingredients_label = Label(text=f"Ingredients : {recipe.get_ing()}")
        students_label = Label(text=f"Student(s) : {recipe.get_student()}")

        # Ajout des infos dans la boîte recipe_box
        recipe_box.add_widget(libelle_label)
        recipe_box.add_widget(ingredients_label)
        recipe_box.add_widget(students_label)

        return recipe_box


if __name__ == "__main__":

    # Initialisation des valeurs et de la fenêtre
    fridge = []
    student = []
    recipes = []
    ingredients = {}
    food_profiles = []
    Config.set('graphics', 'width', '700')
    Config.set('graphics', 'height', '500')

    # Début du lancement du programme
    while True:
        print("1. Encode your food profile.\n2. View Food Profiles.\n3. See the fridge.\n4. Add foods.\n5. Remove "
              "foods.\n6. Encode a recipe.\n7. History of recipes.\n8. Quit.")

        choice = input("What do you want to do? (type the number): ")
        if choice == "1":
            # Demande des informations de l'utilisateur
            lastname = input("Enter your name: ")
            firstname = input("Enter your first name: ")
            weight = int(input("Enter your weight: "))
            height = int(input("Enter your height (in cm): "))
            age = int(input("Enter your age: "))
            gender = input("Enter your gender (F or M): ")
            diet = input("Enter your diet (carnivorous, omnivorous, vegetarian, vegetalian, vegan): ")
            allergy = input("Enter your possible allergies: ")

            # Création du profil alimentaire
            food_profile = FoodProfile(firstname, lastname, diet, gender, age, weight, height, allergy)
            food_profiles.append(food_profile)

            # Visualisation du profil alimentaire
            ProfileApp().run()

        elif choice == "2":
            # Profils alimentaires encodés
            if not food_profiles:
                print("No food profile was encoded.")
            else:
                for profile in food_profiles:
                    print(profile)

        elif choice == "3":
            # Contenu du frigo
            if not fridge:
                print("The fridge is empty.")
            else:
                for food in fridge:
                    print(food)

        elif choice == "4":
            # Demande des informations d'un aliment à mettre dans le frigo
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

            # Création de l'aliment
            food = Food(libelle, food_type, nutriscore, origin, caloric, nutritional_values, expiration_date)
            fridge.append(food)

            # Visualisation des informations de l'aliment
            FoodApp().run()

        elif choice == "5":
            print("In Progress")
            pass

        elif choice == "6":
            # Demande des informations d'une recette
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

            # Création de la recette
            recipe = Recipe(libelle, ingredients, student)
            recipes.append(recipe)
            RecipeApp().run()

        elif choice == "7":
            # Recettes encodées
            if not recipes:
                print("No recipes have yet been encoded.")
            else:
                for recipe in recipes:
                    print(recipe)
        elif choice == "8":
            # Quitter le programme
            print("Thank you for using our program !")
            break
        else:
            print("Choose a number between 1 and 8")
