from Obstacles import *
from Object import *
from math import *


class Player(Obj):
    def __init__(self, screen, pos_center, file, velocity, angle, scale):
        super().__init__(screen, pos_center, file, velocity, angle, scale)
        self.rotate('x', 180)
        
    def update(self) -> None:
        """
        Функция обрабатывает все нажатия клавиш для управления перемещением объекта
        Также здесь вызываются функции move() и rotate() по необходимости

        :param get_pressed - массив со всеми нажатиями клавиш (надо передавать pg.key.get_pressed())
        """
        rotation_angle = 3
        if pg.key.get_pressed()[pg.K_a] and (self.pos_center.x - self.max_dist) > 0:
            self.velocity.x = -5
            if self.angle.z >= -25:
                self.rotate('z', -rotation_angle)
            self.pos_center += self.velocity
        elif pg.key.get_pressed()[pg.K_d] and (self.pos_center.x + self.max_dist) < 800:  #придумать что-то с шириной
            self.velocity.x = 5
            if self.angle.z <= 25:
                self.rotate('z', rotation_angle)
            self.pos_center += self.velocity
        else:
            if abs(self.angle.z) >= 0.1:
                self.rotate('z', -rotation_angle * self.angle.z / abs(self.angle.z))
            else:
                self.angle.z = 0



    def shoot(self):
        """
        Функция вызывается в "main.py" и отвечает за периодическое создание пульвк
        """
        return Bullet(self.screen, self.pos_center, self.file, pg.Vector3(0, 0, 1), 0)


if __name__ == '__main__':
    print('Не тот файл, надо запустить "main.py"')
