class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self) -> str:
            return self.name + ' ' + self.surname

    def get_total_income(self) -> int:
        return self._income.get('wage') + self._income.get('bonus')

if __name__ == '__main__':
    scientist = Position('Иван', 'Васильевич', 'Профессор', 80000, 25000)
    laborant = Position('Петька', ' ', 'Лаборант', 40000, 15000)
    print(scientist.get_full_name()), print(scientist.get_total_income())
    print(laborant.get_full_name()), print(laborant.get_total_income())
