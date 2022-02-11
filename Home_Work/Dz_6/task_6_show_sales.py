import sys

PRICE_FILE = "bakery.csv"

def file_reader(start, end):

    with open(PRICE_FILE, 'r', encoding="utf-8") as show_list:


        if start > 0:
            for _ in range(start - 1):
                show_list.readline()

        if end > 0:
            for _ in range(abs(end - start) + 1):
                yield show_list.readline().replace("\n", "")
        else:
            for line in show_list:
                yield line.replace("\n", "")




input_start = 0
input_end = 0

if len(sys.argv) >= 2 and sys.argv[1].isdigit():
    input_start = int(sys.argv[1])

if len(sys.argv) == 3 and sys.argv[2].isdigit():
    input_end = int(sys.argv[2])

for i in file_reader(input_start, input_end):
    print(i.replace('.',','))