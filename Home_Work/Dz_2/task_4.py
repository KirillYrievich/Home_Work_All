
original_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

def greeting(list):
    for i in list:
        split_lines = i.split()
        wrong_names = split_lines.pop()
        correct_names = f' Привет, {wrong_names.title()}!'
        print(correct_names)


greeting(original_list)

