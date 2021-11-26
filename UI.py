import pygame as pg
from Button import *
from Text import *


BLACK = (0,0,0)

class UI:
    def __init__(self, screen):
        """
        :param screen - экран, нужно для отрисовки объектов
        """

        self.screen =  screen
        self.UI_elements = []

    def add_button(self, screen, bg_color: tuple, color: tuple, pos, width: int, height: int, size: int, phrase: str) -> None:
        """
        Добавляет экземпляр класса "Кнопка" в массив всех элементов

        :param screen, color, pos, width, height - требуются для создания экземпляра
        класса Button
        """
        self.UI_elements.append(Button(screen, bg_color, color, pos, width, height, size, phrase))


    def add_text(self, screen, color, pos, size: int, phrase: str) -> None:
        """
        Добавляет экземпляр класса "Текст" в массив всех элементов

        :param screen, color, pos, size, phrase - требуются для создания экземпляра
        класса Text
        """
        self.UI_elements.append(Text(screen, color, pos, size, phrase))

    def update(self, function: bool) -> None:
        """
        Функция обрабатывает все события, нужно для вызва функции on_click()

        :param events - массив со всеми событиями, нужно для обработки нажатий
        """
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i in self.UI_elements:
                        if i.type == "button":
                            i.on_click(function) # доделать эту фигню!!!
        return function

    def draw(self) -> None:
        """
        Функция вызывает функцию draw() у всез элементов из массива UI_elements
        """
        for i in self.UI_elements:
            i.draw()


if __name__ == '__main__':
    print('Не тот файл, надо запустить "main.py"')
