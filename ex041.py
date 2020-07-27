from datetime import datetime
ano_nasc = int(input('Ano de nascimento: '))
today = datetime.now()
ano_atual = today.year
idade = ano_atual - ano_nasc
if idade <= 9:
    print('Classificação do atleta: MIRIM.')
elif idade <= 14:
    print('Classificação do atleta: INFANTIL.')
elif idade <= 19:
    print('Classificação do atleta: JÚNIOR.')
elif idade <= 25:
    print('Classificação do atleta: SÊNIOR.')
else:
    print('Classificação do atleta: MASTER.')


