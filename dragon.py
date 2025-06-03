class Monster:
    def __init__(self, name : str, health : int, attack_power : int):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, attack): 
       print("namn attackerar target") 

class Vampire(Monster):
    def __init__(self, name : str, health : int, attack_power : int):

class Dragon(Monster):
    def __init__(self, name : str, health : int, attack_power : int):

    Monster = Monster("Monster", 600, 300)
    Vampire = Vampire("Vampire", 400, 120)
    Dragon = Dragon("Dragon", 1000, 300)
