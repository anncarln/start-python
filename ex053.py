# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.

phrase = str(input('Digite a frase que desejar: ')).strip()
phrase1 = frase.upper().replace(' ', '')

print(f'O inverso de {phrase1} é {phrase1[::-1]}')

if phrase1[0] == phrase1[-1]:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo.')








