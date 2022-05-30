# 1 минута
one_minute = 60
# 1 час
one_hour = 3600
# 1 день
one_day = 86400

duration = int(input('Введите продолжительность времени в сек: '))
if duration < 0:
    print('число отрицательное')
elif duration // one_minute == 0:
    print(f'{duration} сек')
elif duration // one_minute > 0 and duration // one_hour == 0:
    print(f'{(duration // one_minute) } мин {duration % one_minute} сек')
elif duration // one_hour > 0 and duration // one_day == 0:
    print(end=f'{duration // one_hour} час {(duration % one_hour) // 60} мин ')
    print(f'{duration % one_minute} сек')
else:
    print(end=f'{duration // one_day} дн {(duration % one_day) // 3600} час ')
    print(f'{(duration % one_hour) // 60} мин {duration % one_minute} сек')
