from food import Food
import argparse

parser = argparse.ArgumentParser = argparse.ArgumentParser(
    description='Simulate a virtual fridge for students in a flat.')
args = parser.parse_args()

if __name__ == "__main__":
    fridge = {}
    num = 1
    while True:
        print("1. Encoder son profil alimentaire\n2. Voir son frigo\n3. Ajouter des aliments\n4. Supprimer des "
              "aliments\n5. Avoir des recettes\n6. Historique des recettes\n7. Quitter")

        choice = input("Que voulez vous faire ? (taper le numéro) ")

        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            response = "oui"
            while response.lower() == "oui":
                fridge["aliment " + str(num)] = {}
                libelle = input("Entrer le nom de l'aliment: ")
                food_type = input("Entrer le type de l'aliment: ")
                nutriscore = input("Entrer le nutriscore de l'aliment: ")
                origin = input("Entrer l'origine de l'aliment: ")
                caloric = int(input("Entrer le nombre de calorie de l'aliment: "))
                nutritional_values = int(input("Entrer les valeurs nutritives de l'aliment: "))
                expiration_date = input("Entrer la date de péremption (format AAAA-MM-DD): ")
                food = Food(libelle, food_type, nutriscore, origin, caloric, nutritional_values, expiration_date)
                print(food)
                num += 1
                response = input("Voulez-vous encore insérer un aliment ? (si oui : taper oui/si non : taper sur une autre "
                                 "touche) ")
        elif choice == '4':
            pass
        elif choice == '5':
            pass
        elif choice == '6':
            pass
        elif choice == '7':
            break
        else:
            print("Choisissez un numéro entre 1 et 7")
