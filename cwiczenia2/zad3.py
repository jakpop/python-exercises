import csv


def average(fileRead, fileWrite):
    file1 = open(fileRead, 'r', newline='')
    file2 = open(fileWrite, 'w', newline='')
    rows = []
    sum_avg = 0
    counter_avg = 0

    for row in csv.reader(file1):
        row_str = ', '.join(row)
        rows.append(row_str)

    j = 1
    for i in range(len(rows)):
        current_row = rows[i]
        if j != len(rows):
            next_row = rows[j]

        sum_avg += float(current_row.split(":")[1])
        counter_avg += 1

        if current_row[0:3] != next_row[0:3]:
            csv.writer(file2).writerow(current_row[:3] + " " + current_row[7:11] + " : " + '{0:.2f}'.format(sum_avg / counter_avg))
            sum_avg = 0
            counter_avg = 0
        elif current_row[0:3] == next_row[0:3] and j == len(rows):
            csv.writer(file2).writerow([current_row[:3] + " " + current_row[7:11] + " : " + '{0:.2f}'.format(sum_avg / counter_avg)])

        j += 1

    file1.close()
    file2.close()


average('APC Historical Data.csv', "apc_wyniki.csv")
