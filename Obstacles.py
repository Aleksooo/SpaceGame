from Object import *


class Enemy(Obj):
    def __init__(self, screen, pos_center):
        super().__init__(screen, pos_center)

class Bullet(Obj):
    def __init__(self, screen, pos_center):
        super().__init__(screen, pos_center)

class Coin(Obj):
    def __init__(self, screen, pos_center):
        super().__init__(screen, pos_center)


if __name__ == '__main__':
    print('Не тот файл, надо запустить "main.py"')
