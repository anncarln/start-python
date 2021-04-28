cadastro = dict()
gol = []

cadastro['nome'] = input("Nome: ")
total_partidas = int(input(f"Quantas partidas {cadastro['nome']} jogou? "))

for c in range(0, total_partidas):
    gol.append(int(input(f"\tQuantos gols na partida {c}? ")))

cadastro['gols'] = gol
cadastro['total'] = sum(gol)

print(cadastro)

for k, v in cadastro.items():
    print(f"O campo {k} tem valor {v}")

print(f"O jogador {cadastro['nome']} jogou {total_partidas} partidas.")

for i, v in enumerate(gol):
    print(f"\t=> Na partida {i+1}, fez {3} gols.")
print(f"Foi um total de {cadastro['total']} gols.")
