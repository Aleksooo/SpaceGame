from Edge import *
import pygame as pg
from math import cos, sin, radians


class Obj:
    def __init__(self, screen, pos_center, file, velocity, angle, scale):
        """
        :param screen - экран, нужно для отрисовки объектов
        :param pos_center - позиция центра объекта
        """

        self.screen = screen
        self.scale = scale
        self.coords = read_data(file)  # сюда надо считать данные о гранях из файла "Player_model.txt"
        for i in self.coords:
            i.A *= scale
            i.B *= scale
            
        self.projected_coords = []
        self.pos_center = pos_center
        self.velocity = velocity
        self.max_dist = max(max(i.A.length(), i.B.length()) for i in self.coords)
        self.angle = angle
        self.file = file

    def update(self) -> None:
        """
        Здесь вызываются функции move() и rotate() по необходимости
        """
        self.move()
        self.rotate()


    def move(self) -> None:
        """
        Функция двигает объект влево или вправо и также проверяет,
        чтобы объект не выходил на пределы экрана
        """
        self.pos_center += self.velocity


    def rotate(self, ax, angle) -> None:
        """
        Функция проходит по всем элементам массива coords и поворачивает их
        вдоль оси объекта на угол angle
        (было бы классно сделать поворот через комплексные числа)

        :param angle - угол поворота
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




    def collide_сoin(self, coins: list):
        """
        Проверка столкновения с "монетами"

        :param coins - массив со всеми "монетами", находящимися на экане

        Возвращает массив "монет" с которыми столкнулся
        """
        collided_coins = []
        for i in coins:
            if (self.pos_center - i.pos_center).length() <= self.max_dist + i.max_dist:
                collided_coins.append(i)
        return(collided_coins)


    def collide_enemy(self, enemies: list):
        """
        Проверка столкновения с "вражескими кораблями"

        :param enemies - массив со всеми "вражескими кораблями", находящимися на экане

        Возвращает массив "вражеских кораблей" с которыми столкнулся
        """
        collided_enemies = []
        for i in enemies:
            if (self.pos_center - i.pos_center).length() <= self.max_dist + i.max_dist:
                collided_enemies.append(i)
        return (collided_enemies)

    def collide_bullet(self, bullets: list):
        """
        Проверка столкновения с "пулями"

        :param bullets - массив со всеми "пулями", находящимися на экане

        Возвращает массив "пуль" с которыми столкнулся
        """
        collided_bullets = []
        for i in bullets:
            if ((self.pos_center - i.A).length() <= self.max_dist) or ((self.pos_center - i.B).length() <= self.max_dist):
                collided_bullets.append(i)
        return(collided_bullets)

    def draw(self) -> None:
        """
        Функция отрисовывает все линии из массива projected_coords
        !!!Вызывать только после проектирования в классе Engine!!! 
        """
        pos_center_v2 = pg.Vector2(self.pos_center.x, self.pos_center.y)
        for i in self.projected_coords:
            pg.draw.line(self.screen, i[2], pos_center_v2 + i[0], pos_center_v2 + i[1], i[3])


if __name__ == '__main__':
    print('Не тот файл, надо запустить "main.py"')
