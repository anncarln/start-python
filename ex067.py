n = 0

while True:
    n = int(input('Quer ver a tabuada de qual número? '))

    print('-' * 30)
    if n < 0:
        break

    for c in range(1, 10+1):
        print(f'{n} x {c} = {n * c}')
    print('-' * 30)

print('Programa de Tabuada encerrado. Volte sempre!')
