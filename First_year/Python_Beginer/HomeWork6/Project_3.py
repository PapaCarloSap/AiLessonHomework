class Worker:
    name = ''
    surname=''
    position=''
    _income=dict()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{self._income["wage"] + self._income["bonus"]}'

position = Position('Ivan', 'Ivanov', 'Any', 100, 50)
print(position.name)
print(position.surname)
print(position.position)
print(position._income)
print(position.get_full_name())
print(position.get_total_income())