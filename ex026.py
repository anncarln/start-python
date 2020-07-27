frase = str(input('Digite a frase que você deseja analisar: ')).strip()
frase1 = frase.upper()
print(f"A letra A aparece {frase1.count('A')} vezes nessa frase")
print(f"A primeira letra A apareceu na posição {frase1.find('A')+1}")
print(f"A última letra A apareceu na posição {frase1.rfind('A')+1}")






