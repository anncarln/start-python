def leiaInt(msg):
    valor = input(msg)
    if valor.isdecimal():
        return valor
    else:
        print(f'Valor inválido. Digite um número inteiro!')
        return leiaInt(msg)


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')