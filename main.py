import pygame as pg
from Engine import *
from Obstacles import *
from Player import *
from Terrain import *
from UI import *
from AI import *


WIDTH, HEIGHT = 800, 600
FPS = 60

BG = (45,64,89)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TEAL = (0, 128, 128)


class App:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()

        self.enemies = []
        self.enemies_to_die = []
        self.bullets = []
        self.bullets_to_die = []
        self.coins = []
        self.coins_to_die = []
        self.UI = UI(self.screen)

        self.score = 0

        self.control_vars = {'in_menu': True, 'in_game': False, 'in_pause': False}
        self.create_menu()

        self.lift = HEIGHT

        self.Engine = Engine(WIDTH, HEIGHT, -30)
        self.Player = Player(self.screen, pg.Vector3(WIDTH/2, self.lift, 0), 'Player_model.txt', pg.Vector3(), pg.Vector3(0, 0, 0), 20)
        self.Terrain = Terrain(self.screen, WIDTH, 550, 20, 12, HEIGHT+20, (34, 139, 34), 1)
        self.AI = AI(self.screen, self.lift, 1300)

    def run(self):
        while True:
            self.create_menu()

            while self.control_vars.get('in_menu'):
                self.clock.tick(FPS)
                self.screen.fill(BG)
                pg.display.set_caption(str(int(self.clock.get_fps())))

                self.control_vars = self.UI.update(self.control_vars)
                self.UI.draw()
                
                ''' Эта фигня работает '''
                keys = pg.key.get_pressed()
                if keys[pg.K_ESCAPE]:
                    exit()

                pg.display.flip()

            self.create_gameUI()

            while self.control_vars.get('in_game'):
                self.clock.tick(FPS)
                self.screen.fill(BG)
                pg.display.set_caption(str(int(self.clock.get_fps())))

                for en in self.enemies_to_die:
                    self.enemies.remove(en)
                self.enemies_to_die = []

                for b in self.bullets_to_die:
                    self.bullets.remove(b)
                self.bullets_to_die = []

                for c in self.coins_to_die:
                    self.coins.remove(c)
                self.coins_to_die = []
                
                ''' ---------------------------------------------------- '''

                self.Terrain.update()
                self.Engine.orthogonal_projection_edge(self.Terrain)
                self.Terrain.draw()

                ''' ---------------------------------------------------- '''

                self.AI.update()
                if self.AI.time_to_spawn_enemy:
                    for en in self.AI.spawn_enemies():
                        self.enemies.append(en)
                if self.AI.time_to_spawn_coin:
                    for c in self.AI.spawn_coins():
                        self.coins.append(c)

                for en in self.enemies:
                    en.update()
                    en.collide_bullet(self.bullets)
                    if en.time_to_die:
                        self.enemies_to_die.append(en)

                    self.Engine.orthogonal_projection_edge(en)
                    self.Engine.orthogonal_projection(en)
                    en.draw()

                ''' ---------------------------------------------------- '''

                for c in self.coins:
                    c.update()
                    if c.time_to_die:
                        self.coins_to_die.append(c)

                    c.rotate('y', 5)
                    self.Engine.orthogonal_projection_edge(c)
                    self.Engine.orthogonal_projection(c)
                    c.draw()
                
                ''' ---------------------------------------------------- '''

                for b in self.bullets:
                    b.update()
                    if b.time_to_die:
                        self.bullets_to_die.append(b)

                    self.Engine.orthogonal_projection_edge(b)
                    self.Engine.orthogonal_projection(b)
                    b.draw()

                
                self.Player.update()
                self.Player.collide_сoin(self.coins)
                if self.Player.time_to_shoot:
                    self.bullets.append(self.Player.shoot())
                self.Engine.orthogonal_projection_edge(self.Player)
                self.Engine.orthogonal_projection(self.Player)
                self.Player.draw()

                self.control_vars = self.UI.update(self.control_vars)
                self.UI.UI_elements[0].update_phrase('Счёт:' + str(self.score)) # Поправить потом!
                self.UI.draw()

                for event in pg.event.get():
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_SPACE:
                            pass

                ''' Эта фигня работает '''
                keys = pg.key.get_pressed()
                if keys[pg.K_ESCAPE]:
                    exit()

                pg.display.flip()
            
    
    def create_menu(self):
        self.UI.restore()
        self.UI.add_text(self.screen, BLACK, pg.Vector2(WIDTH/2-140, 200), 45, "Супер-пупер игра!")
        self.UI.add_button(self.screen, TEAL, BLACK, pg.Vector2(WIDTH/2-100, 400), 200, 40, 30, "Начать", 'play')

    def create_gameUI(self):
        self.UI.restore()
        self.UI.add_text(self.screen, WHITE, pg.Vector2(10, 10), 30, 'Счёт:' + str(self.score))


if __name__ == '__main__':
    app = App()
    app.run()
                