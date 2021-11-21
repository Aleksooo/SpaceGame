from Object import *


class Terrain(Obj):
    def __init__(self, screen, pos_center):
        super().__init__(screen, pos_center)

    def generate_terrain(self) -> None:
        """
        Функция генерирует сетку и записывает все "грани" в массив coords
        """
        pass

    def update(self) -> None:
        """
        Функция изменяет высоту вершин согласно шуму перлина
        """
        pass


if __name__ == '__main__':
    print('Не тот файл, надо запустить "main.py"')
