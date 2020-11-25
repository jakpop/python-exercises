import datetime
import csv


def remainingExams(fileName):
    file1 = open(fileName, 'r', newline='')
    now = datetime.datetime.now()
    end_of_sesja = datetime.datetime.strptime('12 Feb 2021', '%d %b %Y')
    exam_counter = 0

    for row in csv.reader(file1):
        row_str = ', '.join(row)
        date_str = row_str.split(":")[0]
        exam_date = datetime.datetime.strptime(date_str, '%d %b %Y ')

        if now < exam_date < end_of_sesja:
            exam_counter += 1

    return exam_counter


print(remainingExams('sesjaEgzaminacyjna.csv'))
