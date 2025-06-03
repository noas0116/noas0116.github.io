class vehicle:
    def __init__(self, brand : str, color : str, speed : int):
        self.brand = brand
        self.color = color
        self.speed = speed

        def change_color(self, new_color : str):
            self.change_color = change_color

    def move(self):
       print("VROOM")

    class Car(vehicle):
    def _init_(self, brand, color, speed, trunk_volume):
        super().__init__(brand, color, speed)
        self.trunk_volume = trunk_volume

    class Motorcycle(vehicle):
    def _init_(self, brand, color, speed, trunk_volume):
        super().__init__(brand, color, speed)
        self.trunk_volume = trunk_volume

 car1 = Vehicle("Volvo", "Black", 120, 300)
 mc1 = Vehicle("BMW", "Red")