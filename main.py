import pygame as pg
from Engine import Engine
from Obstacles import *
from Player import *
from UI import *
import sys

WIDTH, HEIGHT = 800, 600
FPS = 60

BG = (230, 230, 250)
BLACK = (0, 0, 0)
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

        self.in_menu = True
        self.in_game = False
        self.in_pause = False

        self.Engine = Engine(WIDTH, HEIGHT, 60)
        self.Player = Player(self.screen, pg.Vector3(WIDTH/2, HEIGHT/2, -50), 'Player_model.txt', pg.Vector3(), pg.Vector3(0, 0, 0), 20)

    def run(self):
        while True:
            self.create_menu()
            pg.display.flip()
            while self.in_menu:
                self.clock.tick(FPS)
                self.screen.fill(BG)
                pg.display.set_caption(str(int(self.clock.get_fps())))

                self.UI.update([self.in_game])
                self.UI.draw()
                
                self.Player.update()
                self.Engine.orthogonal_projection(self.Player)
                self.Player.draw()

                for event in pg.event.get():
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_SPACE:
                            print('lol')
                            
                    if event.type == pg.QUIT:
                        sys.exit()

                ''' Эта фигня работает '''
                keys = pg.key.get_pressed()
                if keys[pg.K_ESCAPE]:
                    exit()
                

                pg.display.flip()
            
            for event in pg.event.get():
                    if event.type == pg.QUIT:
                        exit()
            
            pg.display.flip()
    
    def create_menu(self):
        self.UI.add_text(self.screen, BLACK, pg.Vector2(300, 200), 30, "Супер-пупер игра!")
        self.UI.add_button(self.screen, TEAL, BLACK, pg.Vector2(200, 400), 200, 40, 15, "Начать")


if __name__ == '__main__':
    app = App()
    app.run()
                