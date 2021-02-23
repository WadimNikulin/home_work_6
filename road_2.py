class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def road_weight(self):
        weight = (self._length * self._width * 25 * 5) / 1000
        return f"{self._length} м * {self._width} м * 25 кг * 5 см = {int(weight)} т"


a = Road(6000, 20)
print(a.road_weight())
