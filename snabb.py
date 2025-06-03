uttryck = input("skriv din beräkning: ")

uttryck_split = uttryck.split(" ")

operator = uttryck_split[1]
nummer1 = int(uttryck_split[0])
nummer2 = int(uttryck_split[2])

if operator == '+':
    print(nummer1 + nummer2)

elif operator == '-':
    print(nummer1 - nummer2)

if operator == '*':
    print(nummer1 * nummer2)

if operator == '/':
    print(nummer1 / nummer2)


