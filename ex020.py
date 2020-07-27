import random
n1 = str(input('Digite o nome do aluno(a): '))
n2 = str(input('Digite o nome do aluno(a): '))
n3 = str(input('Digite o nome do aluno(a): '))
n4 = str(input('Digite o nome do aluno(a): '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)




