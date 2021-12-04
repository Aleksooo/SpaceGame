import pygame as pg


class Text:
    def __init__(self, screen, color, pos, size: int, phrase: str):
        """
        :param screen - экран, нужно для отрисовки объектов
        :param color - цвет текста
        :param pos - позиция левого верхнего угла текста
        :param size - размер шрифта текста
        :param phrase - текст, который будет отрисовываться
        """

        self.type = "text"
        self.screen = screen
        self.color = color
        self.pos = pos
        self.size = size

        self.f = pg.font.Font(None, size)
        self.text = self.f.render(phrase, True, self.color)

    def update_phrase(self, phrase: str) -> None:
        """
        Замена текущего текста на новый из переменной "phrase"

        :param phrase - новый текст 
        """
        self.text = self.f.render(phrase, True, self.color)

    def draw(self) -> None:
        """
        Отрисовка текста
        """
        self.screen.blit(self.text, self.pos)


if __name__ == '__main__':
    print('Не тот файл, надо запустить "main.py"')