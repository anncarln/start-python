valores = []
pares = []
impares = []

while True:
    valores.append(int(input('Digite um valor: ')))
    opcao = input('Quer continuar? [S/N] ')

    if opcao in 'Nn':
        break

for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print(valores)
print(pares)
print(impares)
