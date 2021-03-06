class Cell:
    __count: int

    def __init__(self, count: int):
        assert count > 0, 'Кол-во ячеек должно быть больше 0'
        self.__count = count

    def __add__(self, other: 'Cell'):
        self.validate_item(other)
        value = self.count + other.count
        return Cell(value)

    def __sub__(self, other: 'Cell'):
        self.validate_item(other)
        value = self.count - other.count
        assert value > 0, 'Разность ячеек меньше 0'
        return Cell(value)

    def __mul__(self, other: 'Cell'):
        self.validate_item(other)
        value = self.count * other.count
        return Cell(value)

    def __truediv__(self, other: 'Cell'):
        self.validate_item(other)
        value = round(self.count / other.count)
        return Cell(value)

    def __str__(self):
        return str(self.__count)

    def validate_item(self, other):
        assert isinstance(other, self.__class__), 'Взаимодействие возможно только между клетками'

    @property
    def count(self) -> int:
        return self.__count

    @staticmethod
    def make_order(cell_object: 'Call', count_per_row: int) -> str:
        items = '*' * cell_object.count
        chunks = [
            items[idx:idx + count_per_row]
            for idx in range(0, len(items), count_per_row)
        ]
        return '\n'.join(chunks)


a = Cell(10)
b = Cell(5)
c = Cell(15)

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(Cell.make_order(c, 5))
