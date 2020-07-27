lista_palavras = ('aprender', 'programar',
                  'linguagem', 'python',
                  'gratis', 'curso',
                  'estudar', 'trabalhar',
                  'praticar', 'mercado',
                  'programador', 'futuro')

for palavra in lista_palavras:
    print(f'\nNa palavra {palavra.upper()} temos ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')
