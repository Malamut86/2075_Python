import sys
import json
from itertools import zip_longest


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    with open(path_users_file, 'r', encoding='utf-8') as users, open(path_hobby_file, 'r', encoding='utf-8') as hobby:
        s = []
        f = []
        for text1 in users:
            s.append(text1.replace(",", ' ').strip())

    for text2 in hobby:
        f.append(text2.replace(",", ' ').strip())
        if len(s) < len(f):
            sys.exit(1)
            dict_out = prepare_dataset('users.csv', 'hobby.csv')
            with open('task_6_3_result.json', 'w') as fw: json.dump(dict_out, f, ensure_ascii=False)



