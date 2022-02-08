numbers_dict = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять'
}


def num_translate(value: str) -> str:
    """переводит числительное с английского на русский """
    # реализуйте здесь, где хранить необходимые исходные данные определитесь самостоятельно
    str_out = numbers_dict.get(value)
    return str_out


print(num_translate("one"))
print(num_translate("two"))
print(num_translate("three"))
print(num_translate("four"))
print(num_translate("five"))
print(num_translate("six"))
print(num_translate("seven"))
print(num_translate("eight"))
print(num_translate("nine"))
