def convert_time(duration: int) -> str:
    user_time = int(input("Время"))
    if user_time // 60 == 0:
        print(user_time, 'сек')
    elif 0 < user_time // 60 <= 59:
        min = user_time // 60
        sec = user_time - min * 60
        print(min, 'мин', sec, 'сек')
    elif 60 <= user_time // 60 <= 86400:
        hour = user_time // 3600
        min = (user_time - hour * 3600) // 60
        sec = user_time - hour * 3600 - min * 60
        print(hour, 'час', min, 'мин', sec,
        'сек')

    return "верните итоговую строку с результатом"


duration = 400153
result = convert_time(duration)
print(result)