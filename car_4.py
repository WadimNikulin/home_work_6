class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        if self.is_police == False:
            self.is_police = "Гражданский авто"
        if self.is_police == True:
            self.is_police = "Полицейский авто"

    def go(self):
        print(f"{self.name}: Поехали!")

    def stop(self):
        print(f"{self.name}: Стоп!")

    def turn(self, direction):
        print(f"{self.name}: Поворот {direction}")

    def show_speed(self):
        print(f'{self.name} скорость: {self.speed}')


class TownCar(Car):
    '''Городской автомобиль'''

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} превышает скорость')
            print(self.speed)
        else:
            print(self.speed)


class SportCar(Car):
    '''Спортивный автомобиль'''


class WorkCar(Car):
    '''Рабочий автомобиль'''

    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} превышает скорость')
            print(self.speed)
        else:
            print(self.speed)


class PoliceCar(Car):
    '''Полицейский автомобиль'''


bmw = Car(180, "black", "bmw M5", False)
print(bmw.turn("налево"))
print(bmw.is_police)

subaru = SportCar(220, "red", "subaru impreza", False)
print(subaru.show_speed())

toyota = TownCar(90, "braun", "toyota supra", False)
print(toyota.show_speed())

kamaz = WorkCar(55, "yelow", "kamaz kamazow", False)
print(kamaz.show_speed())
print(kamaz.speed)

ford_p = PoliceCar(90, "black", "ford police", True)
print(ford_p.name)
print(ford_p.is_police)
print(ford_p.speed)
# не понял почему выводится none
