def summera_siffror(tal): # omvandlar talet till en sträng för att kunna hantera varje siffra individuellt
    summa = sum(int(digit) for digit in str(tal))  # loopar genom siffrorna
    return summa  # returnerar summorna till den ovanför 

# tal = tal1,tal2

tal1 = input("skriv in första talet mannen ") #här skriver du in första talet
tal2 = input("skriv in andra talet också lol ") #här skriver du in andra talet

summa1 = summera_siffror(tal1) #summerar siffrorna för summa 1
summa2 = summera_siffror(tal2) #summerar siffrorna för summa 1

print(f"summan av {tal1} är {summa1}") # f" funktionen ger oss möjlighet att använda variabler i en print command typ
print(f"summan av {tal2} är {summa2}") # så här till exempel så printar vi summorna av talena efter den har summerat dem


print(f"{summa1} == {summa2} -> {summa1 == summa2}") #här kollar den om summorna är lika eller inte

# true = ja talet är lika
# false = nej talena är olika

# hjälp sidor:
# https://blog.finxter.com/5-best-ways-to-find-the-sum-of-all-digits-of-a-given-number-in-python/
# https://www.w3schools.com/python/python_howto_add_two_numbers.asp
# https://realpython.com/lessons/f-strings/