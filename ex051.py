a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

n = 10  # Quantidade de termos

an = a1 + (n - 1)*r  # Fórmula para descobrir o enésimo termo

for c in range(a1, an + 1, r):
    print(c, end=' ')

