valor_casa = float(input('Qual é o valor da casa que você pretende financiar? '))
salário_comprador = float(input('Qual é a sua renda mensal? '))
tempo_pagamento = int(input('Em quantos anos você irá pagar a casa? '))
parcela_mensal = valor_casa / (tempo_pagamento * 12)
if parcela_mensal > 30/100 * salário_comprador:
    print('Infelizmente não podemos conceder esse empréstimo a você nessse momento.')
else:
    print('Podemos conceder esse empréstimo a você.')


