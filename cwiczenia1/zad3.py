import numpy as np


def zad3(lista):
    lista.reverse()
    for i in range(0, len(lista)):
        if i % 2 == 0:
            print(lista[i])


numbers = np.arange(1, 11).tolist()
zad3(numbers)
