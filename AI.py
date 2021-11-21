from Obstacles import *


class AI:
    def __init__(self):
        self.paterns = []

    def update(self):
        """
        Вызывает функции spawn_enemy и spawn_coins соглассно таймеру
        """
        pass

    def spawn_enemies(self, patern: list) -> list[Enemy]:
        """
        Возвращает массив из "вражеских кораблей" согласно данным из массива patern
        """
        pass

    def spawn_coins(self, patern: list) -> list[Coin]:
        """
        Возвращает массив из "Монет" согласно данным из массива patern
        """
        pass


if __name__ == '__main__':
    print('Не тот файл, надо запустить "main.py"')
