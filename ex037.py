import math
num = int(input('Digite um número inteiro: '))
num2 = int(input("Escolha uma das bases para a conversão:\n [1] converter para BINÁRIO\n [2] converter para HEXADECIMAL"
                 "\n [3] converter para OCTAL\n Sua opção: "))
if num2 == 1:
    print(f'O número {num} convertido para BINÁRIO é {bin(num)[2:]}')
elif num2 == 2:
    print(f'O número {num} convertido para HEXADECIAL é {hex(num)[2:]}')
elif num2 == 3:
    print(f'O número {num} convertido para OCTAL é {oct(num)[2:]}')
else:
    print('Opção inválida. Tente novamente.')
