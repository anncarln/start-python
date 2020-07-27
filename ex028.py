from random import randint #Importa a biblioteca random
from time import sleep #Importa a biblioteca time
computador = randint(0, 5) #Faz o computador sortear um número
print('-=-' * 20)
print('Vou pensar em um número! Tente adivinhar...')
print('-=-' * 20)
num = float(input('Digite um número entre 0 e 5: '))
print('Processando...')
sleep(2)
if num == computador:
    print('Parabéns! Você acertou!')
else:
    print(f'Ops, você errou! Eu pensei no número {computador}')

