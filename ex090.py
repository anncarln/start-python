dados = dict()

dados['nome'] = input('Nome: ')
dados['média'] = float(input(f'Média de {dados["nome"]}: '))

if dados['média'] >= 7:
    dados['situação'] = 'Aprovado'
elif 5 <= dados['média'] < 7:
    dados['situação'] = 'Recuperação'
else:
    dados['situação'] = 'Reprovado'

for k, v in dados.items():
    print(f'\t- {k} é igual a {v}')
