import pickle
import sys
import csv
from itertools import zip_longest


def str_func(some_list, new_list):
    for i in some_list:
        i = ' '.join(i)
        new_list.append(i)
    return new_list


key_list = []
value_list = []
result = []

with open('users.csv', 'r', encoding='utf-8') as f1, open('hobby.csv', 'r', encoding='utf-8') as f2:
    key, value = list(csv.reader(f1)), list(csv.reader(f2))
    str_func(key, key_list)
    str_func(value, value_list)
    if len(key_list) >= len(value_list):
        result = dict(zip_longest(key_list, value_list))
    else:
        sys.exit(1)

result_task = 'result_task_3.data'

with open(result_task, 'wb') as f3:
    pickle.dump(result, f3)

with open(result_task, 'rb') as f4:
    result_finish = pickle.load(f4)
    print(result_finish)
