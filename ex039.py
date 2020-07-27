from datetime import datetime
anonasc = int(input('Em que ano você nasceu? '))
today = datetime.now()
anoatual = today.year
idade = anoatual - anonasc
if idade > 18:
    print(f'Já passou da hora de se alistar. O alistamente deveria ter sido feito há {idade - 18} anos.')
elif idade < 18:
    print(f'Ainda não está na hora de se alistar. O alistamento deverá ser feito daqui há {18 - idade} anos.')
elif idade == 18:
    print('Está na hora de se alistar.')





