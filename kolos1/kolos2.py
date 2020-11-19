import numpy as np


def mergePar(list1, list2):
    lst = []
    len1 = len(list1)
    len2 = len(list2)

    for index in range(max(len1, len2)):
        if index + 1 <= len1 and list1[index] % 2 == 0:
            lst += [list1[index]]

        if index + 1 <= len2 and list2[index] % 2 == 0:
            lst += [list2[index]]

    return lst


lista1 = np.arange(1, 11).tolist()
lista2 = np.arange(100, 115).tolist()

print(mergePar(lista1, lista2))
