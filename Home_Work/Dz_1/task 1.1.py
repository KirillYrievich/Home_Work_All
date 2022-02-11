duration = int (input("Введите время в секундах: "))

seconds = duration % 60
minutes = (duration // 60) % 60
hours = ((duration // 60) // 60) % 24
days = duration // 86400

if duration < 60:
    print(seconds, "cek")
elif duration > 60 and duration < 3600:
    print(f'{minutes} мин {seconds} сек ')
elif duration > 3600 and duration < 86400:
    print(f'{hours} час {minutes} мин {seconds} сек ')
else:
    print(f'{days} дн {hours} час {minutes} мин {seconds} сек ')

