import random

kort = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King',
'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King',
'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King',
'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

spelare1 = []
spelare2 = []
spelare3 = []

spelare1_poäng = 0
spelare2_poäng = 0
spelare3_poäng = 0

spelare_tur = 1

for i in range (7):
    random_kort = random.choice(kort)
    spelare1.append(random_kort)
    kort.remove(random_kort)


for i in range (7):
    random_kort = random.choice(kort)
    spelare2.append(random_kort)
    kort.remove(random_kort)

for i in range (7):
    random_kort = random.choice(kort)
    spelare3.append(random_kort)
    kort.remove(random_kort)

while len(spelare1) != 0 and len(spelare2) != 0 and len(spelare3) != 0:
    while True:
        if len(spelare1) == 0:
            if len(kort) != 0:
                random_kort = random.choice(kort)
                spelare1.append(random_kort)
                kort.remove(random_kort)
                print("Spelare 1 tog ett kort från sjön", kort)
            else:
                print("Skippar spelare 1 ")
                break

        print("välj ett kort spelare 1", spelare1)
        kort_val = input()
        print("välj en spelare")
        spelare_val = input()

        if spelare_val == "2": 
            if kort_val in spelare2:
                spelare2.remove(kort_val)
                spelare1.append(kort_val)
                print("Dom hade det kortet")
            else:
                random_kort = random.choice(kort)
                spelare1.append(random_kort)
                kort.remove(random_kort)
                print("Finns i sjön!")
                break

        elif spelare_val == "3":
            if kort_val in spelare3:
                spelare3.remove(kort_val)
                spelare1.append(kort_val)
                print("Dom hade det kortet")  

            else:
                random_kort = random.choice(kort)
                spelare1.append(random_kort)
                kort.remove(random_kort)
                print("Finns i sjön!")
                break

        else:
            print("Eminem, den spelaren finns inte")

    while True:
        if len(spelare2) == 0:
            if len(kort) != 0:
                random_kort = random.choice(kort)
                spelare2.append(random_kort)
                kort.remove(random_kort)
                print("Spelare 2 tog ett kort från sjön", kort)
            else:
                print("Skippar spelare 2")
                break
        print("välj ett kort spelare 2", spelare2)
        kort_val = input()
        print("välj en spelare")
        spelare_val = input() 

        if spelare_val == "1": 
            if kort_val in spelare1:
                spelare1.remove(kort_val)
                spelare2.append(kort_val)
                print("Dom hade det kortet bombaclat")
            else:
                random_kort = random.choice(kort)
                spelare2.append(random_kort)
                kort.remove(random_kort)
                print("Finns i sjön!!!!")
                break

        elif spelare_val == "3":
            if kort_val in spelare3:
                spelare3.remove(kort_val)
                spelare2.append(kort_val)
                print("Dom hade det kortet")

            else:
                random_kort = random.choice(kort)
                spelare2.append(random_kort)
                kort.remove(random_kort)
                print("Bombaclaat den finns i sjön")
                break


        else:
            print("Papa noel, den spelaren finns inte")

    while True:
        if len(spelare3) == 0:
            if len(kort) != 0:
                random_kort = random.choice(kort)
                spelare3.append(random_kort)
                kort.remove(random_kort)
                print("Spelare 3 tog ett kort från sjön", kort)
            else:
                print("Skippar spelare 3")
                break
        print("välj ett kort spelare 3", spelare3)
        kort_val = input()
        print("välj en spelare")
        spelare_val = input()

        if spelare_val == "2": 
            if kort_val in spelare2:
                spelare2.remove(kort_val)
                spelare3.append(kort_val)
                print("haha dom hade det kortet")
            else:
                random_kort = random.choice(kort)
                spelare3.append(random_kort)
                kort.remove(random_kort)
                print("DEN FINNS I SJÖN!!!")
                break

        elif spelare_val == "1":
            if kort_val in spelare1:
                spelare1.remove(kort_val)
                spelare3.append(kort_val)
                print("dom hade det kortet")

            else:
                random_kort = random.choice(kort)
                spelare3.append(random_kort)
                kort.remove(random_kort)
                print("yo den finns i sjön!")
                break


        else:
            print("eminem den spelaren finns inte")