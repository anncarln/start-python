v = float(input('Qual é a velocidade? '))
v1 = float(v) - 80
if v > 80:
    print(f'MULTADO! Você excedeu o limite que é de 80Km/h. O valor da multa a ser pago é de R${7 * v1 :.2f}')
print('Tenha um bom dia! Dirija com segurança!')
