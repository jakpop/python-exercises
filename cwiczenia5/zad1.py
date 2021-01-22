import pandas as pd

data = pd.read_csv('abalone.data')


def delete_and_sort(dataframe, parameter):
    dataframe = dataframe.drop(columns=['M', '15'])
    dataframe = dataframe.sort_values(by=[parameter])

    return dataframe


print(delete_and_sort(data, '0.095'))
