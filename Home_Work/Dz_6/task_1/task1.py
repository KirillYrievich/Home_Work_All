# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).


# нужно импортировать библиотеку requests, с помощью метода get получить у сервера ответ,сохранить его в переменную
# (например response), у ответа есть свойство text, соответственно response.text будет иметь тип str,
# а дальше уже из строки доставать, что вам нужно

import requests


response = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
text = response.text

with open ('text.txt', 'w', encoding="utf-8") as file:
    file.write(text)


def parse_log(pth_file):

    if pth_file:
        with open(pth_file,"r",encoding="utf-8") as file:
            for line in file:
                ip = line.split(" - - ")[0]
                rsp_and_pth = line.split('"')[1]
                rsp = rsp_and_pth.split()[0]
                pth = rsp_and_pth.split()[1]
                yield(ip, rsp, pth)
                # print(ip, rsp, pth)

a = parse_log("text.txt")
# for e in a:
#     print(e)
print(next(a))
print(next(a))
print(next(a))

