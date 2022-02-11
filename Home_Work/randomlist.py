import random


def get_random():
    list = input("Введите список чисел: ")
    print(random.choice(list))
    return list


if __name__ == "__main__":
    get_random()

