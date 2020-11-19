import random

def zad2():
    size = int(input())
    lista = [1, 5, 222, "a", "222", True, False]
    lista2 = []

    for i in range(size):
        lista2.append(random.choice(lista))

    podziel(lista)


def podziel(lista):
    list_int = []
    list_string = []
    list_boolean = []
    for i in range(len(lista)):
        if isinstance(lista[i], int) and not isinstance(list[i], bool):
            list_int.append(lista[i])
        if isinstance(lista[i], str):
            list_string.append(lista[i])
        if isinstance(lista[i], bool):
            list_boolean.append(lista[i])

    print(list_int)
    print(list_string)
    print(list_boolean)


zad2()