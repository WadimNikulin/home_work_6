class Stationery:
    '''канцелярская принадлежность'''
    title = "Канцелярская принадлежность"
    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    '''ручка'''
    def draw(self):
        print("Запуск отрисовки ручкой")

class Pencil(Stationery):
    '''карандаш'''
    def draw(self):
        print("Запуск отрисовки карандашом")


a = Stationery()
print(a.title)
print(a.draw())

b = Pen()
print(b.title)
print(b.draw())

c = Pencil()
print(c.title)
print(c.draw())