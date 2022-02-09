def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""
    # пишите реализацию своей программы здесь
    str_out = "здесь полученная после всех преобразования строковая переменная"
    return str_out

elements = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for find_numbers in elements:
    if find_numbers.isdigit():
        find_numbers = int(find_numbers)
    print(find_numbers, type(find_numbers))
p = '+'
for find_numbers in elements:
    if p in find_numbers:
        print(find_numbers)

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
result = ""
while i < len(my_list):
    if (my_list[i].startswith(('+', '-')) and my_list[i][1:].isdigit()) or my_list[i].isdigit():
        my_list[i] = my_list[i].zfill(2 + 0 ** (abs(my_list[i].find('-') + my_list[i].find('+') + 1)))
        my_list.insert(i, '"')
        i += 1
        my_list.insert(i + 1, '"')
        i += 1
        result += ''.join(my_list[i - 2:i + 1])
    else:
        result += my_list[i]
    result += ' '
    i += 1
print(result)



