import random


def zad1():
    lista = []
    for i in range(10):
        lista.append(random.randrange(10, 20))
        if lista[i] % 2 == 0 and lista[i] % 3 == 0:
            print(lista[i])


zad1()
