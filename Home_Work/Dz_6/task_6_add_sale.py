import sys

PRICE_FILE = "bakery.csv"

prices = sys.argv[1:]

with open(PRICE_FILE, "a", encoding="utf-8") as price_list:
    print(*prices, sep="\n", file=price_list)
