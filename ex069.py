print('-' * 25)
print('CADASTRE UMA PESSOA')
print('-' * 25)

cont0 = cont1 = cont2 = 0

while True:
    age = int(input('Idade: '))
    gender = ' '

    # Caso o usuário digite qualquer outra letra a não ser F ou M, o programa continurá perguntando a opção.
    while gender not in 'MF':
        gender = str(input('Sexo: [F/M] ')).upper().strip()[0]

    if age > 18:
        cont0 += 1

    if gender == 'M':
        cont1 += 1

    if gender == 'F' and age < 20:
        cont2 += 1

    option = ' '
    # Caso o usuário digite qualquer outra letra a não ser S ou N, o programa continurá perguntando a opção.
    while option not in 'SN':
        option = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if option == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {cont0}')
print(f'Ao todo temos {cont1} homens cadastrados.')
print(f'E temos {cont2} mulheres com menos de 20 anos.')

