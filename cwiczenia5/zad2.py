import pandas as pd

data = pd.read_csv('abalone.data')


def mean_and_median(dataframe):
    dataframe = dataframe.drop(columns=['M', '15'])
    means = []
    medians = []

    for column in dataframe.columns:
        means.append(dataframe[column].mean())
        medians.append(dataframe[column].median())

    return means, medians


print(mean_and_median(data))
