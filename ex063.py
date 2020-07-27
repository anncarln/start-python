print('Sequência de Fibonacci')
print('-=' * 15)

termo = int(input('Quantos termos você quer mostrar? '))

t1 = 0 #  o primeiro e o segundo termo já são conhecidos
t2 = 1

print(f'{t1} -> {t2}', end='')

cont = 3
while cont <= termo:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM.')