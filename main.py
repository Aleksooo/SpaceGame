import pygame as pg
from Engine import Engine
from Obstacles import *
from Player import *
from Terrain import Terrain
from UI import *
import sys

WIDTH, HEIGHT = 800, 600
FPS = 60

BG = (230, 230, 250)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TEAL = (0, 128, 128)


class App:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()

        self.enemies = []
        self.bullets = []
        self.coins = []
        self.UI = UI(self.screen)

        self.score = 0

        self.control_vars = {'in_menu': True, 'in_game': False, 'in_pause': False}
        self.create_menu()

        self.Engine = Engine(WIDTH, HEIGHT, -30)
        self.Player = Player(self.screen, pg.Vector3(WIDTH/2, HEIGHT-100, 0), 'Player_model.txt', pg.Vector3(), pg.Vector3(0, 0, 0), 25)
        self.Terrain = Terrain(self.screen, WIDTH, 550, 20, 12, HEIGHT+20, (34, 139, 34), 1)

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
                
                self.Terrain.update()
                self.Engine.orthogonal_projection(self.Terrain)
                self.Terrain.draw()

                self.Player.update()
                self.Engine.orthogonal_projection(self.Player)
                self.Player.draw()

                self.control_vars = self.UI.update(self.control_vars)
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
        self.UI.add_text(self.screen, BLACK, pg.Vector2(10, 10), 30, 'Счёт:' + str(self.score))


if __name__ == '__main__':
    app = App()
    app.run()
                