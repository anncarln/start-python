def vote(birth):
    from datetime import date
    """
    Importar dentro de uma função economiza memória
    porque a classe date só vai ficar dentro da função."""
    current_year = date.today().year
    age = (current_year - birth)
    if 16 <= age < 18 or age > 70:
        return f'Com {age} anos: VOTO OPCIONAL'
    elif age < 16:
        return f'Com {age} anos: NÃO VOTA'
    else:
        return f'Com {age} anos: VOTO OBRIGATÓRIO'


year = int(input('Em que ano você nasceu?: '))
print(vote(year))
