def gen_of_people():
    i = 0
    j = 0
    while i < len(tutors):
        if i >= len(klasses):
            yield (tutors[j], None)
            i += 1
            j += 1
            break
        else:
            yield (tutors[j], klasses[i])
            i += 1
            j += 1


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Кирилл', 'Жора'
]

klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

for gen in gen_of_people():
    print(gen)

a = gen_of_people()

print(type(a))
