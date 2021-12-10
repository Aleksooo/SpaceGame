from Object import *
from Edge import *

class Enemy(Obj):
    def __init__(self, screen, pos_center, file, velocity, angle):
        super().__init__(screen, pos_center, file, velocity, angle)

class Bullet(Obj):
    def __init__(self, screen, pos_center, file, velocity, angle):
        super().__init__(screen, pos_center, file, velocity, angle)
        self.coords = [Edge(pg.Vector3(0, 0, 0), pg.Vector3(0, 0, 1), (0, 0, 0), 5)]  #сделать параметр для цвета и толщины
class Coin(Obj):
    def __init__(self, screen, pos_center, file, velocity, angle):
        super().__init__(screen, pos_center, file, velocity, angle)


if __name__ == '__main__':
    print('Не тот файл, надо запустить "main.py"')
