import pygame as pg
from Text import *


class Button():
    def __init__(self, screen, bg_color: tuple, color: tuple, pos, width: int, height: int, size: int, phrase: str, function: str):
        """
        :param screen - экран, нужно для отрисовки объектов
        :param color - цвет кнопки
        :param pos - позиция левого верхнего угла кнопки
        :param width, height - ширина и высота кнопки
        """
        self.type = "button"
        self.screen = screen
        self.bg_color = bg_color
        self.color = color
        self.size = size
        self.pos = pos
        self.width, self.height = width, height
        self.function = function

        self.text = Text(self.screen, color, pg.Vector2(), size, phrase)
        twidth = self.text.text.get_width()
        theight = self.text.text.get_height()
        tpos = pg.Vector2(self.pos.x + self.width/2 - twidth/2, self.pos.y + self.height/2 - theight/2)
        self.text.pos = tpos

    def on_click(self, control_vars):
        """
        Функция проверяет нажатие на кнопку и выполняет функцию "function"
        при нажатии

        :param function - функция для исполнения
        """
        mouse_pos = pg.mouse.get_pos()
        if self.pos.x < mouse_pos[0] < (self.pos.x + self.width):
            if self.pos.y < mouse_pos[1] < (self.pos.y + self.height):
                if self.function == 'play':
                    return {'in_menu': False, 'in_game': True, 'in_pause': False, 'end_game': False}
                elif self.function == 'pause':
                    return {'in_menu': False, 'in_game': False, 'in_pause': True, 'end_game': False}

        return control_vars

    def draw(self):
        """
        Отрисовка самой кнопки и текста внутри неё
        """
        pg.draw.polygon(self.screen, self.bg_color, [[self.pos.x, self.pos.y], [self.pos.x + self.width, self.pos.y], 
                                               [self.pos.x +self.width, self.pos.y + self.height], [self.pos.x, self.pos.y + self.height]])
        self.text.draw()


if __name__ == '__main__':
    print('Не тот файл, надо запустить "main.py"')
