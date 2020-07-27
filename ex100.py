from random import randint


def sort():
    numbers = list()
    c = 0
    while c < 5:
        a = randint(0, 10)
        c += 1
        numbers.append(a)
    print(numbers)
    return numbers


def sumPair(numbers):
    cont = 0
    for v in numbers:
        if v % 2 == 0:
            cont += v
    print(cont)


numberslist = sort()
sumPair(numberslist)
