"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta

def print_days():
    dt_now = datetime.now()
    print(dt_now.strftime('%d.%m.%Y'))
    delta_day, delta_30_day = timedelta(days=1), timedelta(days=30)
    dt = dt_now - delta_day
    dt_30 = dt_now - delta_30_day
    print(dt.strftime('%d.%m.%Y'))
    print(dt_30.strftime('%d.%m.%Y'))


def str_2_datetime(date_string):
    date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    return date_dt

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
