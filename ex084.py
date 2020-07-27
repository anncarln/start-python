cadastros = list()
cadastro = list()
peso = list()

while True:
    cadastro.append(input('Nome: '))
    cadastro.append(float(input('Peso: ')))
    cadastros.append(cadastro[:])
    peso.append(cadastro[1])
    cadastro.clear()

    opcao = input('Deseja continuar? [S/N] ')

    if opcao in 'Nn':
        break

print(f'{len(cadastros)} pessoas foram cadastradas.')
print(f'O maior peso foi de {max(peso)}. Peso de ', end='')
for p in cadastros:
    if p[1] == max(peso):
        print(f'[{p[0]}]', end='')

print()
print(f'O menor peso foi de {min(peso)}. Peso de ', end='')
for p in cadastros:
    if p[1] == min(peso):
        print(f'[{p[0]}]', end='')
