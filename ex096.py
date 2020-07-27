def area(width, length):
    return width * length


print('Controle de Terrenos')
print('-'*23)

w = int(input('Largura (m): '))
l = int(input('Comprimento (m): '))

a = area(w, l)

print(f'A área do seu terreno de {w}x{l} é de {a}')
