
translator = {
    'zero' : 'ноль',
    'one' : 'один',
    'two' : 'два',
    'three' : 'три',
    'four' : 'четыре',
    'five' : 'пять',
    'six' : 'шесть',
    'seven' : 'семь',
    'eight' : 'восемь',
    'nine' : 'девять',
    'ten' : 'десять'
}

key = input("Напишите число текстом на англ. от 1 до 10: ")

def num_translate(dict):
    print(dict.get(key))

num_translate(translator)