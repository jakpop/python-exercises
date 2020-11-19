import csv


def countChars(fileName):
    file = open(fileName, 'r')
    counter = 0
    for row in csv.reader(file):
        strRow = ', '.join(row)
        counter += len(strRow)
    file.close()
    return counter


print(countChars('APC Historical Data.csv'))
