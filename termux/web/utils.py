from datetime import datetime

def toDateTimeobj(date):
    date, time = str(date).split(" ")
    year, month, day = date.split('-')

    time_splitted = time.split(":")
    if len(time_splitted) == 3:
        hour, min, sec = time.split(":")
        if hour == "24":
            hour = "00"
        if min == "60":
            min = "00"
        if sec == "60":
            sec = "00"
        dateobj = datetime(normalizer(year), normalizer(month.lstrip("0")), normalizer(day.lstrip("0")), normalizer(hour.lstrip("0")),
                           normalizer(min.lstrip("0")), normalizer(sec.lstrip("0")))
    else:
        hour, min = time.split(":")
        if hour == "24":
            hour = "00"
        if min == "60":
            min = "00"
        dateobj = datetime(normalizer(year), normalizer(month.lstrip("0")), normalizer(day.lstrip("0")), normalizer(hour.lstrip("0")),
                           normalizer(min.lstrip("0")))
    return dateobj


def normalizer(string):
    string = string.lstrip("0")
    if len(string) == 0:
        string = 0
    else:
        string = int(string)
    return string

