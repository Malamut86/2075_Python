def thesaurus(*args, bool=True) -> dict:


    if bool:
        args = sorted(list(args))

    dict_out = {}
    for words in args:
        dict_value = dict_out.setdefault(words[0], list())
        if words not in dict_value:
            dict_value.append(words)
            dict_out[words[0]] = dict_value

    return dict_out
print(thesaurus("Иван", "Мария", "Петр", "Илья", "Анна"))

