
def thesaurus(*args):
    dict = {}
    for name in args:
        if dict.get(name[0]):
            dict[name[0]].append(name)
        else:
            dict[name[0]] = [name]
    print(dict)
    return dict


thesaurus("Коля","Вова","Саня","Ваня","Валя","Клава")

