salário = float(input('Qual é o valor do salário? '))
if salário > 1250:
    print(f'Você passará a receber {(10/100 * salário) + salário}')
else:
    print(f'Você passará a receber {(15/100 * salário) + salário}')
