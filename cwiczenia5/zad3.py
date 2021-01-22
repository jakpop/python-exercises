import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('abalone.data')


def dyskretyzacja(dataframe):
    dataframe = dataframe.drop(columns=['M', '15'])
    print(dataframe)

    for column in dataframe.columns:
        dataframe[column] = pd.cut(dataframe[column], bins=[0, 0.5, np.inf], labels=[0, 1])

    dataframe['0.455'].hist()
    plt.show()
    return dataframe


print(dyskretyzacja(data))