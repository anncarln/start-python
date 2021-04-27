from datetime import datetime

dados = dict()

dados["nome"] = input("Nome: ")
ano_nasc = int(input("Ano de nascimento: "))
dados["idade"] = datetime.now().year - ano_nasc
dados["ctps"] = int(input("Carteira de Trabalho (0 não tem): "))

if dados["ctps"] != 0:
  dados["contratação"] = int(input("Ano de contratação: "))
  dados["salário"] = float(input("Salário: R$"))
  dados["aposentadoria"] = dados["idade"] + ((dados["contratação"] + 35) - datetime.now().year)

for k, v in dados.items():
  print(f"\t- {k} tem valor {v}")
