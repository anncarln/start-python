from random import randint
from time import sleep

valores = []
sorteios = []

jogos = int(input('Quantos jogos você quer que eu sorteie? '))

for c in range(0, jogos):
    for n in range(0, 6):
        valor = randint(0, 60)

        if valor not in valores:
            valores.append(valor)
    sorteios.append(valores[:])
    valores.clear()

for i, c in enumerate(sorteios):
    print(f'Jogo {i+1}: {sorted(c)}')
    sleep(1.0)
