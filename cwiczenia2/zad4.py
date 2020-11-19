import csv


def averageByMonthAndYear(fileRead, month_prefix, year):
    file1 = open(fileRead, 'r', newline='')
    year_str = str(year)
    sum_avg = 0
    counter_avg = 0

    for row in csv.reader(file1):
        row_str = ', '.join(row)
        if row_str[0:3] == month_prefix and year_str in row_str:
            sum_avg += float(row_str.split(":")[1])
            counter_avg += 1

    file1.close()
    print(month_prefix + " " + year_str + " : " + '{0:.2f}'.format(sum_avg / counter_avg))


averageByMonthAndYear("APC Historical Data.csv", "Sep", 2016)
