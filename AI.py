from Obstacles import *
import random

class AI:
    def __init__(self, screen, distance):
        self.time_to_spawn_enemy = False
        self.time_to_spawn_coin = False
        self.time_enemy = 0
        self.time_coin = 0
        self.delay_enemy = 60
        self.delay_coin = 90
        self.screen = screen
        self.patterns = [[pg.Vector3(100, 300, distance), pg.Vector3(300, 300, distance), pg.Vector3(500, 300, distance), pg.Vector3(700, 300, distance)],
                         [pg.Vector3(100, 300, distance + 150), pg.Vector3(300, 300, distance + 100), pg.Vector3(500, 300, distance + 50), pg.Vector3(700, 300, distance)],
                         [pg.Vector3(100, 300, distance + 100), pg.Vector3(250, 300, distance + 50), pg.Vector3(400, 300, distance), pg.Vector3(550, 300, distance + 50), pg.Vector3(700, 300, distance + 100)]]

    def update(self):
        """
        Вызывает функции spawn_enemy и spawn_coins соглассно таймеру
        """
        if self.time_enemy == self.delay_enemy:
            self.time_enemy = 0
            self.time_to_spawn_enemy = True
        self.time_enemy += 1
        if self.time_coin == self.delay_coin:
            self.time_coin = 0
            self.time_to_spawn_coin = True
        self.time_coin += 1

    def spawn_enemies(self) -> list[Enemy]:
        """
        Возвращает массив из "вражеских кораблей" согласно данным из массива pattern
        """
        enemies = []
        for i in random.choice(self.patterns):
            enemies.append(Enemy(self.screen, i, 'Enemy_model.txt', pg.Vector3(0, 0, -5), 0, 20))
        self.time_to_spawn_enemy = False
        return enemies

    def spawn_coins(self) -> list[Coin]:
        """
        Возвращает массив из "Монет" согласно данным из массива pattern
        """
        coins = []
        x = random.randint(50, 750)
        coins.append(Coin(self.screen, pg.Vector3(x, 300, 500), 'Coin_model.txt', pg.Vector3(0, 0, -5), 0, 20))
        self.time_to_spawn_coin = False
        return coins


if __name__ == '__main__':
    print('Не тот файл, надо запустить "main.py"')
