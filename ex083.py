expressao = str(input('Digite a expressão: '))

parenteseaberto = []
parentesefechado = []

for c in expressao:
    if c in '(':
        parenteseaberto.append(c)
    elif c in ')':
        parentesefechado.append(c)

if len(parenteseaberto) == len(parentesefechado):
    print('A expressão é válida!')
else:
    print('A expressão é inválida!')

