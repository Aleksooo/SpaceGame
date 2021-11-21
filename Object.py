from Edge import *
import pygame as pg


class Obj:
    def __init__(self, screen, pos_center):
        """
        :param screen - экран, нужно для отрисовки объектов
        :param pos_center - позиция центра объекта
        """

        self.screen = screen
        self.coords = [] # сюда надо считать данные о гранях из файла "Player_model.txt"
        self.projected_coords = []
        self.pos_center = pos_center

    def update(self) -> None:
        """
        Здесь вызываются функции move() и rotate() по необходимости
        """
        pass

    def move(self) -> None:
        """
        Функция двигает объект влево или вправо и также проверяет,
        чтобы объект не выходил на пределы экрана
        """
        pass

    def rotate(self, ax, angle) -> None:
        """
        Функция проходит по всем элементам массива coords и поворачивает их
        вдоль оси объекта на угол angle
        (было бы классно сделать поворот через комплексные числа)

        :param angle - угол поворота
        """
        pass

    def collide_сoin(self, coins: list):
        """
        Проверка столкновения с "монетами"

        :param coins - массив со всеми "монетами", находящимися на экане

        Возвращает массив "монет" с которыми столкнулся
        """
        pass

    def collide_enemy(self, enemies: list):
        """
        Проверка столкновения с "вражескими кораблями"

        :param enemies - массив со всеми "вражескими кораблями", находящимися на экане

        Возвращает массив "вражеских кораблей" с которыми столкнулся
        """
        pass

    def collide_bullet(self, bullets: list):
        """
        Проверка столкновения с "пуляти"

        :param bullets - массив со всеми "пулями", находящимися на экане

        Возвращает массив "пуль" с которыми столкнулся
        """
        pass

    def draw(self) -> None:
        """
        Функция отрисовывает все линии из массива projected_coords
        !!!Вызывать только после проектирования в классе Engine!!! 
        """
        pass


if __name__ == '__main__':
    print('Не тот файл, надо запустить "main.py"')
