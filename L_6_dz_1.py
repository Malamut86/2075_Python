from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    lineAr = line.split()
    return lineAr[0], lineAr[5].lstrip('"'), lineAr[6]


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        list_out.append(get_parse_attrs(line))

pprint(list_out)