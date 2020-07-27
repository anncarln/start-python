valores = []

while True:
    valores.append(int(input('Digite um valor: ')))

    opcao = input('Quer continuar? [S/N] ').upper()

    if opcao in 'Nn':
        break

print(f'Você digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente são {sorted(valores, reverse=True)}')

if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista.')
