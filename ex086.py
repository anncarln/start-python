matriz = [[], [], []]
somapar = somacoluna = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f"Digite um valor para [{l}, {c}]: ")))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()

for l in range(0, 3):
    somacoluna += matriz[l][2]

print(somapar)
print(somacoluna)
print(max(matriz[1]))
