import random
import string


def zad2():
    size = int(input("podaj wielkość listy: "))
    lista = []

    for i in range(size):
        addRandom(lista)

    print(lista)
    podziel(lista)


def podziel(lista):
    list_1 = []
    list_2 = []
    for i in range(len(lista)):
        if isinstance(lista[i], int) or isinstance(lista[i], float):
            list_1.append(lista[i])
        elif isinstance(lista[i], str) or type(lista[i] == bool):
            list_2.append(lista[i])

    print(list_1)
    print(list_2)


def addRandom(lista):
    i = random.randrange(0, 4)
    if i == 0:
        lista.append(randomInt())
    if i == 1:
        lista.append(randomFloat())
    if i == 2:
        lista.append(randomBool())
    if i == 3:
        lista.append(randomString())


def randomInt():
    return int(random.random() * 10)


def randomFloat():
    return random.random() * 10


def randomBool():
    return bool(random.getrandbits(1))


def randomString():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))


zad2()
