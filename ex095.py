cadastro = dict()
jogadores = []
gols = []

while True:
    cadastro.clear()
    gols.clear()
    cadastro['nome'] = input("Nome: ")
    total_partidas = int(input(f"Quantas partidas {cadastro['nome']} jogou? "))

    for c in range(0, total_partidas):
        gols.append(int(input(f"\tQuantos gols na partida {c+1}? ")))

    cadastro['gols'] = gols[:]
    cadastro['total'] = sum(gols)

    jogadores.append(cadastro.copy())

    while True:
        opcao = input('Quer continuar? [S/N] ').upper()[0]

        if opcao in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if opcao == 'N':
        break

print(f'{"cod":<3} {"nome":<15} {"gols":<15} {"total":<15}')

for i, d in enumerate(jogadores):
    print(f'{i:<3} {d["nome"]:<15} {d["gols"]!s:<15s} {d["total"]:<15}')    # !s:s transforma lista em str temporariamente

while True:
    cod = int(input('Mostrar dados de qual jogador? [999 para parar] '))

    if cod == 999:
        break
    else:
        if cod >= len(jogadores):
            print(f'ERRO! Não existe jogador com código {cod}!')
        else:
            print(f'LEVANTAMENTO DO JOGADOR {jogadores[cod]["nome"]}')

            for i, v in enumerate(jogadores[cod]['gols']):
                print(f'No jogo {i+1} fez {v} gols.')

print('>>VOLTE SEMPRE!<<')
