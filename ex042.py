print('-=' * 20)
print('Análise de Triângulos')
print('-=' * 20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if abs(b - c) < a < b + c and abs(c - a) < b < c + a and abs(a - b) < c < a + b:
    print('É possível existir um triângulo.')
    if a == b and a == c and b == c:
        print('O triângulo é EQUILÁTERO.')
    elif a != b and a != c and b != c:
        print('O triângulo é ESCALENO.')
    else:
        print('O triâgulo é ISÓSCELES.')
else:
    print('Não é possível existir um triângulo.')



