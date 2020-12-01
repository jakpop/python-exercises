import datetime


def convertDateFormat(date, date_format):
    date_format = date_format.replace('yyyy', '%Y')
    date_format = date_format.replace('yy', '%y')
    date_format = date_format.replace('mm', '%m')
    date_format = date_format.replace('dd', '%d')

    return date.strftime(date_format)


dt = datetime.datetime.now()
print(dt)
print(convertDateFormat(dt, "dd/mm/yy"))
