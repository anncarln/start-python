import sys
from time import sleep
a = float(input('Primeiro valor: '))
b = float(input('Segundo valor: '))

opção = 0
maior = 0

while opção != 5:
    print('''         [1] somar
         [2] multiplicar
         [3] maior
         [4] novos números
         [5] sair do programa''')
    opção = int(input('>>>>>>>> Qual é a sua opção? '))

    if opção == 1:
        print(f'O resultado de {a:.0f} + {b:.0f} é {a + b:.0f}.')
    elif opção == 2:
        print(f'O resultado de {a:.0f} x {b:.0f} é {a * b:.0f}.')
    elif opção == 3:
        if a > b:
            maior = a
        else:
            maior = b
            print(f'Entre {a:.0f} e {b:.0f} o maior é {maior:.0f}.')
    elif opção == 4:
        print('Informe os números novamente.')
        a = float(input('Primeiro valor: '))
        b = float(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
        sys.exit(0)
    else:
        print('Opção inválida. Tente novamente.')
    sleep(2)











