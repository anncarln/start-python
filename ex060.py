# Resolução do exercício utilizando o while:
n = int(input('Digite um número para calcular seu Fatorial: '))

f = 1    # fator nulo de multiplicação é 1 (para uma multiplicação limpa, iniciando em 1).

print(f'Calculando {n}! = ', end='')

while n > 0:
    # Essas duas linhas de print servem basicamente para mostrar o cálculo do fatorial na tela.
    print(f'{n}', end='')
    print(' x ' if n > 1 else ' = ', end='')
    # Calculando o resultado do fatorial.
    f *= n      # é a mesma coisa de f = f * n.
    # A cada vez que o laço for executado n perde 1 na contagem.
    n -= 1      # é a mesma coisa de n = n - 1.

print(f'{f}')      # mostra o resultado do fatorial na tela.
