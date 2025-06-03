class Car:
    def __init__(self, brand: str, color: str, speed: int):
        self.brand = brand
        self.color = color
        self.speed = speed

    def __str__(self):
        return f"en {self.color} {self.brand}"
    
    def change_color(self, new_color: str):
        self.color = new_color


volvo1 = Car("Volvo", "svart", 200)

print(volvo1.color)

volvo1.change_color("grön")
print(volvo1)

print(volvo1.speed)

print(volvo1.brand)
