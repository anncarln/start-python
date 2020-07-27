nome = str(input('Digite o seu nome completo: ')).strip().split()
print(f"O seu primeiro nome é {nome.pop(0)}")
print(f"O seu último nome é {nome.pop()}")


