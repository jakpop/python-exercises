import random
import numpy as np


def zad1():
    size = int(input())
    lista = []
    sum = 0
    mediana = 0
    for i in range(size):
        lista.append(random.random())
        sum += lista[i]
        print(lista[i])

    srednia = np.mean(lista)
    print("srednia: ", srednia)
    srednia2 = sum / len(lista)
    print("srednia2: ", srednia2)

    lista.sort()
    print(lista)
    length = int(len(lista))
    if length % 2 == 0:
        mediana = (lista[int((length/2)-1)]+lista[int((length/2))])/2
    else:
        mediana = lista[int(length/2)]

    print("mediana: ", mediana)


zad1()