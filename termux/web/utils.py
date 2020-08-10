from datetime import datetime

def toDateTimeobj(date):
    date, time = str(date).split(" ")
    year, month, day = date.split('-')

    time_splitted = time.split(":")
    if len(time_splitted) == 3:
        hour, min, sec = time.split(":")
        dateobj = datetime(int(year), int(month.lstrip("0")), int(day.lstrip("0")), int(hour.lstrip("0")),
                           int(min.lstrip("0")), int(sec.lstrip("0")))
    else:
        hour, min = time.split(":")
        dateobj = datetime(int(year), int(month.lstrip("0")), int(day.lstrip("0")), int(hour.lstrip("0")),
                           int(min.lstrip("0")))
    return dateobj
