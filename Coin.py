from Edge import *

class Coin:
    def __init__(self, screen, pos_center):
        """
        :param screen - экран, нужно для отрисовки объектов
        :param pos_center - позиция центра объекта
        """
        
        self.screen = screen
        self.coords = [] # сюда надо считать данные о гранях из файла "Coin_model.txt"
        self.projected_coords = []
        self.pos_center = pos_center
    
    def update(self) -> None:
        """
        Функция вызывает функцию move() и все...(немного бесполезная)
        """
        pass

    def move(self) -> None:
        """
        Функция двигает объект
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
