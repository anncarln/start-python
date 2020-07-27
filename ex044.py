print('{:=^40}'.format(' LOJA ANNA CAROLINA '))

preço = float(input('Preço total da sua compra: R$'))

print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

opção = int(input('Qual é a opção? '))

desconto10 = preço - ((10/100) * preço)
desconto5 = preço - ((5/100) * preço)
juros20 = preço + ((20/100) * preço)

if opção == 1:
    print(f'A sua compra no valor de {preço} à vista tem 10% de desconto e sairá por {desconto10}')
elif opção == 2:
    print(f'A sua compra no valor de {preço} no cartão à vista tem 5% de desconto e sairá por {desconto5}')
elif opção == 3:
    print(f'A sua compra sairá pelo mesmo valor de {preço}')
elif opção == 4:
    parcelas = int(input('Número de parcelas: '))
    parcelas1 = (juros20/parcelas)
    print(f'A sua compra no valor de {preço} parcelada para {parcelas}x de R${parcelas1} terá JUROS.\n'
          f'Sua compra vai custar {juros20} no final.')
else:
    print('Opção inválida de pagamento. Tente novamente.')


