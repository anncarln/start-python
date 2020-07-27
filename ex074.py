from random import randint

l = []
c = 0
while c < 5:
    n = randint(0, 10)
    l.append(n)
    c += 1

t = tuple(l)
print(t)
print(f'O menor valor é {sorted(t)[0]}')
print(f'O maior valor é {sorted(t)[4]}')
