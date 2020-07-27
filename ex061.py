print('Gerador de PA')
print('-=' * 10)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 1
while cont <= 10:
    print(f'{a1} -> ', end='')
    a1 += r
    cont += 1
print('FIM.')


