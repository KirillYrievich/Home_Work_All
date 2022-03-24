class Worker:
    def __init__(self, name, surname, position, income={"wage": 1, "bonus": 2}):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.surname} {self.name}')

    def get_total_income(self):
        print(f"Полный доход сотрудника (с премией): {self._income['wage'] + self._income['bonus']} ")


a = Position('Кирилл', 'Афанасьевский', 'Programmer', {'wage': 10, 'bonus': 5})

a.get_full_name()
a.get_total_income()
