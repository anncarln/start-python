from datetime import date
current = date.today().year
count = 0
count1 = 0

for c in range(1, 8):

    birth = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    age = current - birth

    if age >= 18:
        count += 1
    else:
        count1 += 1

print(f'Ao todo tivemos {count} maiores de idade.')
print(f'E também tivemos {count1} menores de idade.')








