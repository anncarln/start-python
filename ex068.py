from random import randint

print('-=' * 15)
print('Jogo do Par ou Ímpar')
print('-=' * 15)

cont = 0

while True:
    option = str(input('Par ou Ímpar? ')).upper().strip()[0]
    n = int(input('Qual número você quer jogar? '))
    computer = randint(0, 10)

    sum = (n + computer)

    print(f'Você jogou {n} e o computador jogou {computer}. O total foi {sum}.')

    if option == 'P':
        if sum % 2 == 0:
            print('Você ganhou!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    elif option == 'I':
        if sum % 2 != 0:
            print('Você ganhou!')
        else:
            print('Você perdeu!')
            break
print(f'GAME OVER! Total de vitórias: {cont}')
