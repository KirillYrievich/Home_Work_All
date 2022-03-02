# Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения
# извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError. Пример:
import re

# def email_parse(email_address):
#     try:
#         # # pattern = re.compile(r'^[А-ЯЁ][а-яё][0-9a-z_]+$]')
#         # pattern = re.compile(r'^([\d\w])')
#         # print(pattern.match(email_address))
#         for i in email_address.split(@):
#             my_dicti[username] = i[0]
#             my_dicti[domain] = i[1]
#
#
#     except:
#         print(lox)
#
# my_dict = {}
#
# email_parse("someone@geekbrains.ru")
# print(my_dict)

a = 'someone@geekbrains.ru'
b = 'afanas.lg2@gmail.com'
MY_DICT = {}

# split_a = a.split('@')

for i in b.split('@'):
    if re.search(r'[2]$', i):
        MY_DICT['username'] = i
        print('Y')
    else:
        MY_DICT['domain'] = i
        print("lox")

print(MY_DICT)