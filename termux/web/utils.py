from datetime import datetime

def toDateTimeobj(date):
    date, time = str(date).split(" ")
    year, month, day = date.split('-')
    hour, min = time.split(":")

    return datetime(int(year), int(month.lstrip("0")), int(day.lstrip("0")), int(hour.lstrip("0")), int(min.lstrip("0")))

