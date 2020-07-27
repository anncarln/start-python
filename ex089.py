dados = []
geral = []

while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    geral.append(dados[:])
    dados.clear()
    opcao = input('Deseja continuar? [S/N] ')
    if opcao in 'Nn':
        break

print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')

for i, c in enumerate(geral):
    media = (c[1] + c[2]) / 2
    print(f'{i:<4}{c[0]:<10}{media:>8.1f}')

nota = int(input('Mostrar nota de qual aluno? (999 interrompe) '))

if nota == 999:
    exit()
else:
    print(f'As notas de {geral[nota][0]} foram {geral[nota][1], geral[nota][2]}')

"""                                           
Outra forma de colocar uma lista dentro da outra:
                                              
while True:                                   
nome = input('Nome: ')                        
nota1 = float(input('Nota 1: ')               
nota2 = float(input('Nota 2: ')               
media = (nota1 + nota2) / 2                   
dados.append([nome, [nota1, nota2], media])"""
