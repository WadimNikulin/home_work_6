from time import sleep
from itertools import cycle


class TrafficLight:
    __color = ["\033[31m {}".format("*"), "\033[33m {}".format("*"), "\033[32m {}".format("*"),
               "\033[37m {}".format("*")]

    def running(self):
        for n in cycle((1, 2, 3)):
            print(self.__color[0])
            print(self.__color[3])
            print(self.__color[3])
            sleep(7)
            print('\n')
            print(self.__color[3])
            print(self.__color[1])
            print(self.__color[3])
            sleep(2)
            print('\n')
            print(self.__color[3])
            print(self.__color[3])
            print(self.__color[2])
            sleep(7)
            print('\n')  # не разобрался как обнулить распечатанное
            # в терминале. задумка была чтобы печаталась
            # тройка знаков цветных. серый - значит светофор не горит.


f = TrafficLight()
print(f.running())
