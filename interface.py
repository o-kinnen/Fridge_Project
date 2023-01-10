from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class FridgeApp(App):
    def build(self):
        self.title = "Fridge"
        profile = BoxLayout(orientation="vertical")

        # Informations du profil encodé
        name = Label(text="Name : ")
        sex = Label(text="Sex : ")
        age = Label(text="Age : ")
        height = Label(text="Height : ")
        diet = Label(text="Diet : ")
        allergy = Label(text="Allergy : ")
        imc = Label(text="IMC : ")
        daily_needed_calories = Label(text="Daily Needed Calories : ")

        # Ajout des infos dans la boîte profile
        profile.add_widget(name)
        profile.add_widget(sex)
        profile.add_widget(age)
        profile.add_widget(height)
        profile.add_widget(diet)
        profile.add_widget(allergy)
        profile.add_widget(imc)
        profile.add_widget(daily_needed_calories)

        return profile

