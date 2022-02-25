import requests

response = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
text = response.text

with open('text.txt', 'w', encoding="utf-8") as file:
    file.write(text)


def parse_log(pth_file):
    if pth_file:
        with open(pth_file, "r", encoding="utf-8") as file:
            for line in file:
                ip = line.split(" - - ")[0]
                rsp_and_pth = line.split('"')[1]
                rsp = rsp_and_pth.split()[0]
                pth = rsp_and_pth.split()[1]
                yield (ip, rsp, pth)
                # print(ip, rsp, pth)


a = parse_log("text.txt")

print(next(a))
print(next(a))
print(next(a))
