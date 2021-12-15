from Obstacles import *
from random import choice, randint

class AI:
    def __init__(self, screen, lift, distance):
        self.time_to_spawn_enemy = False
        self.time_to_spawn_coin = False
        self.time_enemy = 0
        self.time_coin = 0
        self.delay_enemy = randint(150, 180)
        self.delay_coin = randint(80, 120)
        self.screen = screen
        self.lift = lift
        self.distance = distance

        self.patterns = [[pg.Vector3(100, lift, distance), pg.Vector3(300, lift, distance), pg.Vector3(500, lift, distance), pg.Vector3(700, lift, distance)],
                         [pg.Vector3(100, lift, distance + 150), pg.Vector3(300, lift, distance + 100), pg.Vector3(500, lift, distance + 50), pg.Vector3(700, lift, distance)],
                         [pg.Vector3(100, lift, distance + 100), pg.Vector3(250, lift, distance + 50), pg.Vector3(400, lift, distance), pg.Vector3(550, lift, distance + 50), pg.Vector3(700, lift, distance + 100)]]

    
    def update(self):
        """
        Вызывает функции spawn_enemy и spawn_coins соглассно таймеру
        """
        if self.time_enemy == self.delay_enemy:
            self.time_enemy = 0
            self.time_to_spawn_enemy = True
            self.delay_enemy = randint(150, 180)
        self.time_enemy += 1
        
        if self.time_coin == self.delay_coin:
            self.time_coin = 0
            self.time_to_spawn_coin = True
            self.delay_coin = randint(80, 120)
        self.time_coin += 1

    def spawn_enemies(self) -> list[Enemy]:
        """
        Возвращает массив из "вражеских кораблей" согласно данным из массива pattern
        """
        enemies = []
        for i in list(choice(self.patterns)):
            enemies.append(Enemy(self.screen, pg.Vector3(i.x, i.y, i.z), 'Enemy_model.txt', pg.Vector3(0, 0, -5),  pg.Vector3(0, 0, 0), 20))
        self.time_to_spawn_enemy = False
        return enemies

    def spawn_coins(self) -> list[Coin]:
        """
        Возвращает массив из "Монет" согласно данным из массива pattern
        """
        coins = []
        x = randint(50, 750)
        coins.append(Coin(self.screen, pg.Vector3(x, self.lift, self.distance), 'Coin_model.txt', pg.Vector3(0, 0, -5),  pg.Vector3(0, 0, 0), 20))
        self.time_to_spawn_coin = False
        return coins


if __name__ == '__main__':
    print('Не тот файл, надо запустить "main.py"')
