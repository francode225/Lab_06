phrase = input("Entrez une phrase : ")

maj = 0
min = 0
for car in phrase:
    if car.isupper():
        maj += 1
    elif car.islower():
        min += 1

print(f"Majuscules : {maj}")
print(f"Minuscules : {min}")