from time import sleep


def cont(start, end, step):
    if step < 0:
        step *= (-1)

    print(f'Contagem de {start} até {end} de {step} em {step}')
    sleep(2.5)

    if step == 0:
        step = 1

    if start > end:
        for v in range(start, end+1, step * (-1)):
            print(f'{v} ', end='')
            sleep(0.5)
        print('FIM!')
    else:
        for v in range(start, end+1, step):
            print(f'{v} ', end='')
            sleep(0.5)
        print('FIM!')


cont(1, 10, 1)
cont(10, 0, 2)

print('Agora é a sua vez de personalizar a contagem!')

start1 = int(input('Início: '))
end1 = int(input('Fim:    '))
step1 = int(input('Passo:  '))

cont(start1, end1, step1)
