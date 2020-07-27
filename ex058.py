from random import randint
computador = randint(0, 10)
acertos = 0
num = 0

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10! Tente adivinhar...')
print('-=-' * 20)

while num != computador:
    num = float(input('Qual é o seu palpite? '))
    acertos += 1

    if computador > num:
        print('Mais... Tente mais uma vez.')
    if num > computador:
        print('Menos... Tente mais uma vez.')

print(f'Acertou com {acertos:.0f} tentativas. Parabéns!')

# Enquanto a variável contida em "num" for diferente da variável escolhida pelo computador, o programa continuará perguntando
# "Qual é o seu palpite?". Em "acertos += 1", o número de palpites necessários para o acerto são contabilizados. Os ifs testam
# as condições para o jogador continuar colocando inputs até acertar e, quando ele acerta, é impressa uma mensagem de parabéns.









