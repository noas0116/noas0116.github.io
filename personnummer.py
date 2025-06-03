print("ange ditt personnummer:(xxxxxx-xxxx) ")

personummer = input()
alla_nummer = ""
summa = 0
kontroll_siffra = 0

for i in range(len(personummer) - 1):
    print(i)

    if(i % 2 == 0):
        alla_nummer += str(int(personummer[i]) * 2)
    else:
        alla_nummer += personummer[i]

print(alla_nummer)

for num in alla_nummer:
    summa += int(num)


print(summa)

kontroll_siffra =  (10 - (summa % 10)) % 10

print(kontroll_siffra)

if(str(kontroll_siffra) == personummer[-1]):
    print("Dehär är ett giltigt personummer")
else:
    print("dehär är inte ett giltigt personummer")