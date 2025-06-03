ordlista = []
förra_ordet = ""
print("Skriv ett ord för att börja leken :)")

while True:
    ord = input()

    if ord in ordlista :
        print("game over bozo, du använde samma ord")

    

    ordlista.append(ord)
    förra_ordet = ord