nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media < 0.5:
    print('Reprovado.')
elif 5.0 <= media <= 6.9:
    print('Recuperação.')
elif media >= 7:
    print('Aprovado.')

