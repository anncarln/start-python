print('Gerador de PA')
print('-=' * 10)

a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))

cont = 0    # contador
total = 0   # acumulador
n = 10      # o programa inicia mostrando 10 termos, depois o usuário quem vai dizer quantos termos quer visualizar

while n != 0:   # 0 indica que o usuário quer finalizar a visualização dos termos
    total += n      # total = total + n
    while cont <= total:
        print(f'{a1} -> ', end='')
        a1 += r     # a1 = a1 + r
        cont += 1   # cont = cont + 1
    print('PAUSA')
    n = int(input('Quantos termos você quer mostrar a mais? '))

print(f'Progressão finalizada com {total} termos mostrados.')

















