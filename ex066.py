n = s = t = 0

while True:
    n = int(input('Digite um número [999 para parar]: '))

    if n == 999:
        break

    t += 1
    s += n

print(f'Você digitou {t} números e a soma entre eles é {s}.')
