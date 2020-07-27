a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Mais um número, por favor: '))
# Verificando qual é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando qual é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')



