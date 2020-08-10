from datetime import datetime

def toDateTimeobj(date):
    date, time = str(date).split(" ")
    year, month, day = date.split('-')
    hour, min = time.split(":")

    return datetime(int(year), int(month), int(date), int(hour), int(min))
