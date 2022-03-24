class Road:
    def __init__(self, width, length, weight_of_1_sq_m=25, thickness=5):
        self._width = width
        self._length = length
        self.weight_of_1_sq_m = weight_of_1_sq_m
        self.thickness = thickness

    def all_weight(self):
        weight = (self._width * self._length * self.weight_of_1_sq_m * self.thickness) / 1000
        print(f'Масса асфальта состовляет {int(weight)} тонн')


m4 = Road(20, 5000)

m4.all_weight()
