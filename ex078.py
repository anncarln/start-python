valores = []
maior = 0
menor = 0

for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))

    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print(f'Você digitou os valores {valores}.')
print(f'O valor {menor} é o menor valor. E está nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i} ')
print(f'O valor {maior} é o maior valor. E está nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i} ')
