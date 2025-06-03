from nicegui import ui
import random

class Karaktar:
    def __init__(self, gender: str, name: str, age: int, ras: str, work :str, egenskaper : list):
        self.name = name
        self.age = age
        self.gender = gender 
        self.work = work
        self.ras = ras
        self.egenskaper = egenskaper

karaktar_1 = Karaktar("", "", 0, "", "", [])

namn = ["Knut Pung", "Kalle Balle", "Röriga Bengt", "Bosse Andersson", "Hasse Larsson", "Veronica Mugg"]
age = [45, 56, 25, 43, 38, 52]
gender = ["Man", "Kvinna"]
ras = ["Svensk", "Norsk", "Tysk", "Fransk", "Italiensk", "Spansk"]
work = ["Tårtdekoratör", "ICA", "Sotare", "Rörmockare", "Busshafför", "Bärplockare"]
egenskaper = [
    ["Snabb, ", "Sladdrig, ", "Idiot"],
    ["Kreativ, ", "Knepig, ", "Smart"],
    ["Långsam, ", "Huvudlös, ", "Dum i huvudet"],
    ["Bitter, ", "Förrädisk, ", "Rörig"],
    ["Skrikig, ", "Märklig, ", "Förvirrad"],
    ["Rufsig, ", "Tänkande, ", "Dömande"]
]

def skapa_karaktar():
    karaktar_1.name = random.choice(namn)
    karaktar_1.age = random.choice(age)
    karaktar_1.gender = random.choice(gender)
    karaktar_1.ras = random.choice(ras)
    karaktar_1.work = random.choice(work)
    karaktar_1.egenskaper = random.choice(egenskaper)

    name_label.text = karaktar_1.name
    age_label.text = karaktar_1.age
    gender_label.text = karaktar_1.gender
    ras_label.text = karaktar_1.ras
    work_label.text = karaktar_1.work
    egenskaper_label.text = karaktar_1.egenskaper

ui.button('Generera gubbe', on_click=lambda: skapa_karaktar())

name_label = ui.label("")
age_label = ui.label("")
gender_label = ui.label("")
ras_label = ui.label("")
work_label = ui.label("")
egenskaper_label = ui.label("")


ui.run(native=True)