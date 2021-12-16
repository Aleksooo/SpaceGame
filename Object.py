from Edge import *
import pygame as pg
from math import cos, sin, radians


class Obj:
    def __init__(self, screen, pos_center, file, velocity, angle, scale):
        """
        :param screen - экран, нужно для отрисовки объектов
        :param pos_center - позиция центра объекта
        :param file - текстовый файл с координатами граней
        :param velocity - скорость объекта
        :param angle - угол поворота объекта
        :param scale - коэффициент пропорциональности для увеличения/уменьшения размеров объекта
        """
        self.screen = screen
        self.scale = scale
        self.coords = read_data(file)  # сюда надо считать данные о гранях из файла "Player_model.txt"
        for i in self.coords:
            i.A *= scale
            i.B *= scale
            
        self.projected_coords = []
        self.pos_center = pos_center
        self.pos_center_v2 = pg.Vector2
        self.velocity = velocity
        self.max_dist = max(max(i.A.length(), i.B.length()) for i in self.coords)
        self.angle = angle
        self.file = file

        self.time_to_die = False

    def update(self):
        """
        Здесь вызываются функции move() и rotate() по необходимости
        """
        if self.pos_center.z <= -200 or self.pos_center.z >= 1500:
            self.time_to_die = True

        self.pos_center += self.velocity

    def move(self):
        """
        Функция двигает объект влево или вправо и также проверяет,
        чтобы объект не выходил на пределы экрана
        """
        self.pos_center += self.velocity

    def rotate(self, ax, angle):
        """
        Функция проходит по всем элементам массива coords и поворачивает их
        вдоль оси объекта на угол angle

        :param angle - угол поворота
        :param ax - ось вокруг которой происходит поворот
        """
        if ax == 'x':
            self.angle.x += angle
        elif ax == 'y':
            self.angle.y += angle
        elif ax == 'z':
            self.angle.z += angle
        
        for i in self.coords:
            if ax == 'x':
                z = complex(i.A.y, i.A.z)
                r = complex(cos(radians(angle)), sin(radians(angle)))
                z_new = z*r
                i.A = pg.Vector3(i.A.x, z_new.real, z_new.imag)
                z = complex(i.B.y, i.B.z)
                r = complex(cos(radians(angle)), sin(radians(angle)))
                z_new = z * r
                i.B = pg.Vector3(i.B.x, z_new.real, z_new.imag)
            elif ax == 'y':
                z = complex(i.A.x, i.A.z)
                r = complex(cos(radians(angle)), sin(radians(angle)))
                z_new = z * r
                i.A = pg.Vector3(z_new.real, i.A.y, z_new.imag)
                z = complex(i.B.x, i.B.z)
                r = complex(cos(radians(angle)), sin(radians(angle)))
                z_new = z * r
                i.B = pg.Vector3(z_new.real, i.B.y, z_new.imag)
            elif ax == 'z':
                z = complex(i.A.x, i.A.y)
                r = complex(cos(radians(angle)), sin(radians(angle)))
                z_new = z * r
                i.A = pg.Vector3(z_new.real, z_new.imag, i.A.z)
                z = complex(i.B.x, i.B.y)
                r = complex(cos(radians(angle)), sin(radians(angle)))
                z_new = z * r
                i.B = pg.Vector3(z_new.real, z_new.imag, i.B.z)

    def collide_сoin(self, coins):
        """
        Проверка столкновения с "монетами"

        :param coins - массив со всеми "монетами", находящимися на экане

        Опускает "флаг" у монет, с которыми произошло столкновение
        """
        collided_coins = []
        for i in coins:
            if (self.pos_center - i.pos_center).length() <= self.max_dist + i.max_dist:
                collided_coins.append(i)
                i.time_to_die = True
                return True
        return False


    def collide_enemy(self, enemies):
        """
        Проверка столкновения с "вражескими кораблями"

        :param enemies - массив со всеми "вражескими кораблями", находящимися на экане

        Опускает "флаг" у врагов с которыми произошло столкновение
        """
        collided_enemies = []
        for i in enemies:
            if (self.pos_center - i.pos_center).length() <= 0.9*(self.max_dist + i.max_dist):
                collided_enemies.append(i)
                return True
        return False

    def collide_bullet(self, bullets):
        """
        Проверка столкновения с "пулями"

        :param bullets - массив со всеми "пулями", находящимися на экане

        Опускает "флаг" у пуль, которые попали во врага
        """
        collided_bullets = []
        for i in bullets:
            if ((self.pos_center - (i.pos_center + i.coords[0].A)).length() <= 0.9*self.max_dist) or ((self.pos_center - (i.pos_center + i.coords[0].B)).length() <= 0.9*self.max_dist):
                collided_bullets.append(i)
                self.time_to_die = True
                i.time_to_die = True
                return True
        return False

    def draw(self):
        """
        Функция отрисовывает все линии из массива projected_coords
        !!!Вызывать только после проектирования в классе Engine!!! 
        """
        for i in self.projected_coords:
            pg.draw.line(self.screen, i[2], self.pos_center_v2 + i[0], self.pos_center_v2 + i[1], i[3])


if __name__ == '__main__':
    print('Не тот файл, надо запустить "main.py"')
