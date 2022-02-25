class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self) -> None:
        return f'{self.name} поехали'

    def stop(self) -> None:
        return f'{self.name} стоп'

    def turn_right(self) -> None:
        return f'{self.name} право'

    def turn_left(self) -> None:
        return f'{self.name} лево'

    def show_speed(self):
        return f'скорость {self.name} авто {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self) -> None:
        print(f'скорость {self.name} авто {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} выше допустимой для городской машины'
        else:
            return f'Скорость {self.name} допустимая для городской машины'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self) -> None:
        print(f'Скорость   {self.name} авто {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} выше допустимой для рабочей машины'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self) -> None:
        if self.is_police:
            return f'{self.name} полиция'
        else:
            return f'{self.name} не полиция'

if __name__ == '__main__':
    Golf = TownCar(40, 'White', 'Гольф', False)
    Cat = WorkCar(41, 'Rose', 'Кэт', False)
    Police = PoliceCar(120, 'Blue', 'Alarm!!! Speed!!!', True)
    Ferrari = SportCar(300, 'Red', 'Феррари', False)

print(Ferrari.show_speed())
print(Police.go())
print(Cat.show_speed())
print(Police.police())
print(Golf.show_speed())
#print(Police.show_speed())
print(Cat.turn_left())
print(Ferrari.turn_right())
print(Golf.stop())


