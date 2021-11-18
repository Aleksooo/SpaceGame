from Edge import *

class Terrain:
    def __init__(self, screen):
        """
        :param screen - экран, нужно для отрисовки объектов
        """
        
        self.screen = screen
        self.coords = []
        self.projected_coords = []

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
    
    def draw(self) -> None:
        """
        Функция отрисовывает все линии из массива projected_coords
        !!!Вызывать только после проектирования в классе Engine!!! 
        """
        pass


if __name__ == '__main__':
    print('Не тот файл, надо запустить "main.py"')
