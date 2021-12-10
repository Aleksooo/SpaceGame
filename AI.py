from Obstacles import *
import random

class AI:
    def __init__(self, screen):
        self.screen = screen
        self.patterns = [[pg.Vector3(100, 300, 500), pg.Vector3(300, 300, 500), pg.Vector3(500, 300, 500), pg.Vector3(700, 300, 500)],
                         [pg.Vector3(100, 300, 1100), pg.Vector3(300, 300, 900), pg.Vector3(500, 300, 700), pg.Vector3(700, 300, 500)],
                         [pg.Vector3(100, 300, 900), pg.Vector3(250, 300, 700), pg.Vector3(400, 300, 500), pg.Vector3(550, 300, 700), pg.Vector3(700, 300, 900)]]

    def update(self):
        """
        Вызывает функции spawn_enemy и spawn_coins соглассно таймеру
        """
        pass

    def spawn_enemies(self) -> list[Enemy]:
        """
        Возвращает массив из "вражеских кораблей" согласно данным из массива pattern
        """
        enemies = []
        for i in random.choice(self.patterns):
            enemies.append(Enemy(self.screen, i, 'Enemy_model.txt', pg.Vector3(0, 0, -1), 0))
        return enemies

    def spawn_coins(self) -> list[Coin]:
        """
        Возвращает массив из "Монет" согласно данным из массива pattern
        """
        coins = []
        x = random.randint(50, 750)
        coins.append(Coin(self.screen, pg.Vector3(x, 300, 500), 'Coin_model.txt', pg.Vector3(0, 0, -1), 0))
        return coins


if __name__ == '__main__':
    print('Не тот файл, надо запустить "main.py"')
