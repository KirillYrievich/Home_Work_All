class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} автомобиль начал движение')

    def show_speed(self):
        print(f'Автомобиль двигаеться со скоростью {self.speed} км/ч')

    def turn(self, direction):
        self.direction = direction
        print(f'Автомобиль повернул {direction}')

    def stop(self):
        print('Автомобиль остановился')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Сбавь скорость! Ограничение по скорости 60 км/ч')
        else:
            print(f'Автомобиль двигаеться со скоростью {self.speed} км/ч')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Сбавь скорость! Ограничение по скорости 40 км/ч')
        else:
            print(f'Автомобиль двигаеться со скоростью {self.speed} км/ч')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


a = TownCar(70, "Чёрный", "BMW")
b = WorkCar(50, "Чёрный", "BMW")
c = SportCar(110, 'Красный', 'Ferrari')
d = PoliceCar(90, 'Белый', 'УАЗ', True)

a.go()
a.show_speed()
b.show_speed()
c.show_speed()
d.show_speed()
a.turn('налево')
a.stop()
print(c.is_police)
print(d.is_police)
