def transfer_list_in_str(list_in: list) -> str:

    list_out = list()
    for element in list_in:
        my_list = element.split()

        str_out = my_list
    return str_out

my_list = ['57.80 ' '46.51 ' '97.00 ' '100.20 ' '45.80 ' '64.15 ' '79.09 ' '120.20 ' '87.08 ' '456.51 ' '197.00 ' '1000.00']
result = transfer_list_in_str(my_list)
print(result)

def convert_extract(list_in: list) -> list:
    list_out = list()
    for element in list_in:
        my_list = element.split(' ')
        i = 1
        j = 2
        list_out.append(f'' + my_list[len(my_list) - j] + 'rrub' + my_list[len(my_list) - i] + 'kkop.')

        return list_out

my_list = ['57 .80', '46 .51', '97 .00', '100 .20', '45 .80', '64 .15', '79 .09', '120 .20', '87 .08', '456 .51', '197 .00', '1000 .00']
result = convert_extract(my_list)
print(result)



