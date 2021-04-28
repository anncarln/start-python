dados = dict()
cadastro = []
somaidades = 0

while True:
    dados.clear()
    dados['nome'] = input('Nome: ')
    while True:
        dados['sexo'] = str(input('Sexo [F/M]: ')).upper()[0]
        if dados['sexo'] in 'FM':
            break
        print('ERRO! Por favor, digite apenas F ou M.')

    dados['idade'] = int(input('Idade: '))

    somaidades += dados['idade']

    cadastro.append(dados.copy())

    while True:
        opcao = input('Quer continuar? [S/N] ').upper()[0]
        if opcao in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if opcao == 'N':
        break

media = (somaidades / len(cadastro))

print(f'A) Ao todo temos {len(cadastro)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for d in cadastro:
    if d['sexo'] in 'F':
        print(d['nome'])
print('D) Lista das pessoas que estão acima da média: ')
for d in cadastro:
    for k, v in d.items():
        if k == 'idade' and v > media:
            print(f'\tnome = {d["nome"]}; sexo = {d["sexo"]}; idade = {d["idade"]}')

print('<< ENCERRADO >>')
