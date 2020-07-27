def fatorial(num, show=None):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número num.
    """
    c = 1
    for v in range(num, 0, -1):
        if show:
            print(v, end='')
            if v > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        c *= v
    return c


print(fatorial(8, show=True))
help(fatorial)
