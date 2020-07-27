t = (('Lápis', '1.75'),
     ('Borracha', '2.00'),
     ('Caderno', '15.90'),
     ('Estojo', '25.00'),
     ('Transferidor', '4.20'),
     ('Compasso', '9.90'),
     ('Mochila', '120.32'),
     ('Canetas', '22.30'),
     ('Livros', '34.90'),
     )

print('-' * 40)
for c in t:
    print(f'{c[0]:.<30}R$ {c[1]:>6}')
print('-' * 40)
