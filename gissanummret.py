import random

nummer = (random.randrange(1,100))

while True:
    try:
        gissning = int(input("gissa nummret 1-100: "))

        if gissning == nummer:
            print("rätt tal!") 
            break
        elif gissning > nummer:
            print("talet är mindre")
        else:
            print("talet är större")
    except ValueError:
        print("dedär är en bokstav mannen")