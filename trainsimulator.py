class Passenger:
    def __init__(self, name: str, destination: int):
        self.name = name
        self.destination = destination

class Wagon:
    def __init__(self, passengers: list[Passenger]):
        self.passengers = passengers

class Train:
    def __init__(self, wagons: list[Wagon], line: int, position: int):
        self.wagons = wagons 
        self.line = line 
        self.position = position
 
class Station:
    def __init__(self, name: str, passengers: list[Passenger]):
        self.name = name
        self.passengers = passengers

class Line:
    def __init__(self, name: str, stops: list[int]):
        self.name = name
        self.stops = stops

stations = [
    Station("Storlien", []),
    Station("Åre", []),
    Station("Helsingborg", []),
    Station("Östersund", [])
]

lines = [
    Line("blåa linjen går på:", [0, 1, 3, 2]),
]
print(lines[0].name)
for  station_pos in lines[0].stops:
    print(stations[station_pos].name)

passengers = ["Pontus", "Olle", "Eminem"]

