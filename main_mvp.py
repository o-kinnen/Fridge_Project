import argparse

parser = argparse.ArgumentParser = argparse.ArgumentParser(
    description='Simulate a virtual fridge for students in a flat.')
args = parser.parse_args()


def bissextile(_year):
    """Teste si une année est bissextile ou non."""
    if _year % 4 == 0 and _year % 100 != 0 or _year % 400 == 0:
        return True
    else:
        return False


def date_is_valid(_day, _month, _year):
    """Teste si une date est valide, et donc, si elle peut exister dans le calendrier"""
    if bissextile(_year):
        february = 29
    else:
        february = 28

    day_in_month = {1: 31,
                    2: february,
                    3: 31,
                    4: 30,
                    5: 31,
                    6: 30,
                    7: 31,
                    8: 31,
                    9: 30,
                    10: 31,
                    11: 30,
                    12: 31}

    # Si la valeur du mois est compris entre 1 et 12
    # Et que le nombre de jours est compris entre 1 et le nombre de jours dans ce mois.
    if (1 <= _month <= 12) and (1 <= _day <= day_in_month[_month]):
        return True
    else:
        return False


if __name__ == "__main__":
    fridge = {}
    num = 1

    while True:
        print("1. Encoder son profil alimentaire\n2. Voir son frigo\n3. Ajouter des aliments\n4. Supprimer des "
              "aliments\n5. Avoir des recettes\n6. Historique des recettes\n7. Quitter")
        choice = input("Que voulez vous faire ? (taper le numéro) ")

        if choice == '1':
            print("en cours")
        elif choice == '2':
            if fridge == {}:
                print("votre frigo est vide")
            else:
                print("mon frigo :", fridge)
        elif choice == '3':
            response = "oui"
            while response.lower() == "oui":
                fridge["aliment " + str(num)] = {}

                name = input("entrer le nom de l'aliment : ")

                while True:
                    expiration_date = input("entrer la date de péremption en format dd/mm/yy : ")
                    day = int(expiration_date[:2])
                    month = int(expiration_date[3:5])
                    year = int(expiration_date[6:])
                    if date_is_valid(day, month, year):
                        break
                    else:
                        print("date invalide")

                while True:
                    nutriScore = input("entrer le nutri-score de l'aliment : ")
                    if nutriScore.upper() == 'A' or nutriScore.upper() == 'B' or nutriScore.upper() == 'C' \
                            or nutriScore.upper() == 'D' or nutriScore.upper() == 'E':
                        break
                    else:
                        print("NutriScore invalide")

                fridge["aliment " + str(num)]["name"] = name
                fridge["aliment " + str(num)]["expiration_date"] = expiration_date
                fridge["aliment " + str(num)]["nutriScore"] = nutriScore
                num += 1
                response = input("voulez vous encore insérer un aliment ? (si oui : taper oui/si non : taper sur un "
                                 "touche) ")

        elif choice == '4':
            print("en cours")
        elif choice == '5':
            print("en cours")
        elif choice == '6':
            print("en cours")
        elif choice == '7':
            break
