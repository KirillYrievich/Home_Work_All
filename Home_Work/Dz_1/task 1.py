
duration = int(input("Введите цифровое значение: "))

day = duration // 86400
hour = duration // 3600
min = duration // 60


def actually_time(duration):

    if duration <= 60:
        print(duration, 'сек')
    elif duration > 60 and duration <= 3600:
        print(f'{min} мин {duration % 60} сек')
    elif duration > 3600 and duration <= 86400:
        hour_min = (duration % 3600) // 60
        hour_sec = (duration % 3600) % 60
        print(f'{hour} час {hour_min} мин {hour_sec} cек')
    else:
        day_hour = (duration % 86400) // 3600
        day_min = ((duration % 86400) % 3600) // 60
        day_sec = ((duration % 86400) % 3600) % 60
        print(f' {day} дн {day_hour} час {day_min} мин {day_sec} cек')

actually_time(duration)
