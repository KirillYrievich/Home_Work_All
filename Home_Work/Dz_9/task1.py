import time


class TrafficLight:
    __base_color = "мигающий жёлтый"

    def ranning(self):
        print("Стой! Горит красный свет")
        time.sleep(7)
        print("Приготовься, загорелся жёлтый свет")
        time.sleep(2)
        print("Вперед!!! Зелёный")


a = TrafficLight()

a.ranning()
