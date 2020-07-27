d = float(input('Qual é a distância em Km da sua viagem? '))
if d <= 200:
    print(f'O valor da passagem é R${0.50 * d :.2f}')
else:
    print(f'O valor da passagem é R${0.45 * d :.2f}')
    
