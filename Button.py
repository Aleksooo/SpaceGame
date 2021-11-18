from Text import *

class Button():
    def __init__(self, screen, color: tuple, pos, width: int, height: int):
        """
        :param screen - экран, нужно для отрисовки объектов
        :param color - цвет кнопки
        :param pos - позиция левого верхнего угла кнопки
        :param width, height - ширина и высота кнопки
        """
        
        self.type = "button"
        self.screen = screen
        self.color = color
        self.pos = pos
        self.width, self.height = width, height

    def create_text(self, color, pos, size: int, phrase: str) -> None:
        """
        Функция создает текст для кнопки

        :param color, pos, size, phrase - эти параметры требуется передать в конструктор класса Text
        """
        self.text = Text(self.screen, color, pos, size, phrase)
        #--> Надо не забыть, что эту функцию надо вызывать сразу после создания экземпляра класса "Button"

    def on_click(self, function) -> None:
        """
        Функция проверяет нажатие на кнопку и выполняет функцию "function"
        при нажатии

        :param function - функция для исполнения
        """
        pass

    def draw(self) -> None:
        """
        Отрисовка самой кнопки и текста внутри неё
        """
        pass


if __name__ == '__main__':
    print('Не тот файл, надо запустить "main.py"')
