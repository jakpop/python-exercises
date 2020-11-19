import numpy as np


def merge(list1, list2):
    lst = []
    len1 = len(list1)
    len2 = len(list2)

    for index in range(max(len1, len2)):
        if index + 1 <= len1:
            lst += [list1[index]]

        if index + 1 <= len2:
            lst += [list2[index]]

    return lst


lista1 = np.arange(1, 11).tolist()
lista2 = ["a", "b", "c", "d", "e", "f", "g", "h"]

print(merge(lista1, lista2))
