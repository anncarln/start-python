print('-=' * 20)
print('Análise de Triângulos')
print('-=' * 20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if abs(b - c) < a < b + c and abs(c - a) < b < c + a and abs(a - b) < c < a + b:
    print('É possível existir um triângulo.')
else:
    print('Não é possível existir um triângulo.')

