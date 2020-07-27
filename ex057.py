sexo = str(input('Informe o sexo [F/M]: ')).strip().upper()[0] # o [0] seleciona a letra que está no íncide correspondente, nesse caso, a primeira letra

while sexo not in 'FM':
    sexo = str(input('Opção inválida. Informe o sexo: ')).strip().upper()[0]

print('Os dados foram salvos com sucesso.')
