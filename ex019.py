import random
nome1 = str(input('Nome do aluno: '))
nome2 = str(input('Nome do aluno: '))
nome3 = str(input('Nome do aluno: '))
nome4 = str(input('Nome do aluno: '))
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')

