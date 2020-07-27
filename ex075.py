t = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))

print(f'Você digitou os valores {t}')

# vezes em que o 9 aparece
print(f'O valor 9 apareceu {t.count(9)} vezes.')

# posição do valor 3
if 3 in t:
    print(f'O valor 3 apareceu na {t.index(3)+1}ª posição.')
else:
    print(f'O valor 3 não apareceu em nenhuma posição.')

# números pares
print('Os valores pares digitados foram ', end='')
for c in t:
    if c % 2 == 0:
        print(f'{c} ', end='')
