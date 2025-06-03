ord = input()

bokstaver = {}

for bokstav in ord:
    if bokstav in bokstaver:
        bokstaver[bokstav] += 1
    else:
        bokstaver[bokstav] = 1

print(bokstaver)