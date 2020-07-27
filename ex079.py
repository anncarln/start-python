valores = []

while True:
    valor = int(input('Digite um valor: '))

    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')

    opcao = input('Quer continuar? [S/N] ').upper()

    if opcao in 'NÃO':
        break

print(f'Você adicionou {sorted(valores)}')


