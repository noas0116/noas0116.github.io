class Pokemon:
    def __init__(self, element: str, name: str, health: float, attack: float, defence: float):
        self.element = element
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence

eldpokemon = Pokemon("fire", "charizzard", 600, 300, 100)
vattenpokemon = Pokemon("water", "gyardos", 400, 120, 200)




def calculate_damage(attacker : Pokemon, defender : Pokemon):
    effect = 1
    if attacker.element == "fire" and defender.element == "water":
        effect = 0.5
    elif attacker.element == "water" and defender.element == "fire":
        effect = 2
    
    return 50 * (attacker.attack / defender.defence) * effect


result = calculate_damage(eldpokemon, vattenpokemon)
print(result)