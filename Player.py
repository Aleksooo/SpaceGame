from Object import *


class Player(Obj):
    def __init__(self, screen, pos_center):
        super().__init__(screen, pos_center)
        
    def update(self, get_pressed) -> None:
        """
        Функция обрабатывает все нажатия клавиш для управления перемещением объекта
        Также здесь вызываются функции move() и rotate() по необходимости

        :param get_pressed - массив со всеми нажатиями клавиш (надо передавать pg.key.get_pressed())
        """
        pass

    def shoot(self):
        """
        Функция вызывается в "main.py" и отвечает за периодическое создание пульвк
        """
        pass


if __name__ == '__main__':
    print('Не тот файл, надо запустить "main.py"')
