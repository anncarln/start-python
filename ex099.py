def bigger(*args):
    if len(args) > 0:
        print(f'O maior valor foi {max(args)}')
    else:
        print('Não foi informado nenhum valor!')


bigger(1, 3, 4, 6, 7)
bigger()
