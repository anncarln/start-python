print('~' * 20)
print('Calculadora de IMC.')
print('~' * 20)
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura * altura)
print('Este é o seu IMC: {:.1f}.'.format(imc))
if imc < 18.5:
    print('De acordo com esse valor, você está abaixo do peso ideal.')
elif imc == 18.5 or imc <= 25:
    print('De acordo com esse valor, você está no peso ideal.')
elif imc == 25 or imc <= 30:
    print('De acordo com esse valor, você está com sobrepeso.')
elif imc == 30 or imc <= 40:
    print('De acordo com esse valor, você está com obesidade.')
else:
    print('De acordo com esse valor, você está com obesidade mórbida. Cuidado!')
