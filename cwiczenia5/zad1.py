import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('abalone.data')


def delete_and_sort(dataframe, parameter):
    dataframe = dataframe.drop(columns=['M', '15'])
    dataframe = dataframe.sort_values(by=[parameter])

    return dataframe


def mean_and_median(dataframe):
    dataframe = dataframe.drop(columns=['M', '15'])
    means = []
    medians = []

    for column in dataframe.columns:
        means.append(dataframe[column].mean())
        medians.append(dataframe[column].median())

    return means, medians


def dyskretyzacja(dataframe):
    dataframe = dataframe.drop(columns=['M', '15'])
    print(dataframe)

    for column in dataframe.columns:
        dataframe[column] = pd.cut(dataframe[column], bins=[0, 0.5, np.inf], labels=[0, 1])

    dataframe['0.455'].hist()
    plt.show()
    return dataframe


def dyskretyzacja2(dataframe, parting):
    dataframe = dataframe.drop(columns=['M', '15'])
    print(dataframe)

    if parting == 2:
        for column in dataframe.columns:
            dataframe[column] = pd.cut(dataframe[column], bins=[0, 0.5, np.inf],
                                       labels=[0, 1])
    if parting == 4:
        for column in dataframe.columns:
            dataframe[column] = pd.cut(dataframe[column], bins=[0, 0.25, 0.5, 0.75, np.inf],
                                       labels=[0.25, 0.5, 0.75, 1])
    if parting == 5:
        for column in dataframe.columns:
            dataframe[column] = pd.cut(dataframe[column], bins=[0, 0.2, 0.4, 0.6, 0.8, np.inf],
                                       labels=[0.2, 0.4, 0.6, 0.8, 1])
    if parting == 10:
        for column in dataframe.columns:
            dataframe[column] = pd.cut(dataframe[column], bins=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, np.inf],
                                       labels=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])

    return dataframe


# print(delete_and_sort(data, '0.095'))
# print(mean_and_median(data))
# print(dyskretyzacja(data))
# print(dyskretyzacja2(data, 5))
