cont = acumu = maior = menor = 0 # se todas as variáveis vão receber os mesmos valores, podemos igualar todas desta forma
p = 'S'

while p in 'Ss':
    n = int(input('Digite um número: '))
    cont += 1
    acumu += n

    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    p = str(input('Quer continuar? [S/N] ').upper().strip()[0])

media = acumu / cont # média não precisa estar dentro do while porque ela vai usar todos os números iterados

print(f'Você digitou {cont} números e a média foi {media}.')
print(f'O maior valor foi {maior} e o menor valor foi {menor}.')
