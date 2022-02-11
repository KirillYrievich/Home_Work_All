
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

n = random.randrange(1, 5)


def get_jokes(n):
    for i in zip(random.sample(nouns, 5), random.sample(adverbs, 5), random.sample(adjectives, 5)):

        if n > 0:
            print(random.sample(i, 3))
            n = n - 1


get_jokes(n)
