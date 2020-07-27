from time import sleep

c = ('\033[m',          # 0 - sem cores
     '\033[1;41m',      # 1 - fundo vermelho
     '\033[1;42m',      # 2 - fundo verde
     '\033[1;107m',     # 3 - fundo branco
     '\033[1;44m')      # 4 - fundo azul


def IntHelp(prmt):
    print(c[3], end='')
    help(prmt)
    print(c[0], end='')


def formatarstr(txt, cor=None):
    print(c[cor], end='')
    print('^' * (len(txt) + 4))
    print(f'  {txt}')
    print('^' * (len(txt) + 4))
    print(c[0], end='')


while True:
    msg = 'SISTEMA DE AJUDA pyHELP'
    formatarstr(msg, 2)
    sleep(1)
    comando = input('Função ou Biblioteca > ')
    if comando.upper() == 'FIM':
        msg2 = 'ATÉ LOGO!'
        formatarstr(msg2, 1)
        break
    else:
        msg1 = f'Acessando o manual do comando \'{comando}\''
        formatarstr(msg1, 4)
        sleep(3)
        print(IntHelp(comando))
