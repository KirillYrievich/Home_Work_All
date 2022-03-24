class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки!')


class Pen(Stationery):
    def draw(self):
        print(f'Рисуем ручкой')


class Pencil(Stationery):
    def draw(self):
        print(f'Делаем штрихи карандашом')


class Handle(Stationery):
    def draw(self):
        print(f'Выделяем маркером')


a = Stationery('Кисть')
b = Pen('Ручка')
c = Pencil('Карандаш')
d = Handle('Маркер')

a.draw()
b.draw()
c.draw()
d.draw()
print(a.title)
print(b.title)
print(c.title)
print(d.title)
