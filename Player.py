from pygame.constants import K_SPACE
from Obstacles import *
from Object import *
from math import *


class Player(Obj):
    def __init__(self, screen, pos_center, file, velocity, angle, scale):
        super().__init__(screen, pos_center, file, velocity, angle, scale)
        self.rotate('z', 180)
        self.angle.z = 0
        
        self.time = 0
        self.shoot_delay = 8

        self.time_to_shoot = False
        
    def update(self):
        """
        Функция обрабатывает все нажатия клавиш для управления перемещением 
        и вращением игрока
        """

        rotation_angle = 3
        if pg.key.get_pressed()[pg.K_a] and (self.pos_center.x - self.max_dist) > 0:
            self.velocity.x = -5
            if self.angle.z >= -25:
                self.rotate('z', -rotation_angle)
            self.pos_center += self.velocity
        elif pg.key.get_pressed()[pg.K_d] and (self.pos_center.x + self.max_dist) < 800:
            self.velocity.x = 5
            if self.angle.z <= 25:
                self.rotate('z', rotation_angle)
            self.pos_center += self.velocity
        else:
            if abs(self.angle.z) >= 0.1:
                self.rotate('z', -rotation_angle * self.angle.z / abs(self.angle.z))
            else:
                self.angle.z = 0

        if pg.key.get_pressed()[pg.K_SPACE]:
            if self.time == self.shoot_delay:
                self.time_to_shoot = True
                self.time = 0
            self.time += 1


    def shoot(self):
        """
        Функция вызывается в "main.py" и отвечает за создание элемента класса Bullet при нажатии игроком на пробел
        """
        self.time_to_shoot = False
        return Bullet(self.screen, pg.Vector3(self.pos_center.x, self.pos_center.y, self.pos_center.z), self.file, pg.Vector3(0, 0, 5), pg.Vector3(0, 0, 0), 0)


if __name__ == '__main__':
    print('Не тот файл, надо запустить "main.py"')
