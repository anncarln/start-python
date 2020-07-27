from random import randint
from time import sleep

lista = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)

print('{:^20}'.format(' Jokenpô online '))
sleep(1)

print('''Suas opções:
[0] PEDRA
[1] PAPEL 
[2] TESOURA''')

jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=' * 13)
print(f'O computador jogou {lista[computador]}')
print(f'O jogador jogou {lista[jogador]}')
print('-=' * 13)

if jogador == 0: # Jogador jogou PEDRA
    if computador == 0:
        print('Empate!')
    elif computador == 1:
        print('Jogador venceu!')
    elif computador == 2:
        print('Jogador venceu!')
    else:
        print('Jogada inválida!')

if jogador == 1: # Jogador jogou PAPEL
    if computador == 0:
        print('Computador venceu!')
    elif computador == 1:
        print('Empate!')
    elif computador == 2:
        print('Computador venceu!')
    else:
        print('Jogada inválida!')

if jogador == 2: # Jogador jogou TESOURA
    if computador == 0:
        print('Computador venceu!')
    elif computador == 1:
        print('Jogador venceu!')
    elif computador == 2:
        print('Empate!')
    else:
        print('Jogada inválida!')
