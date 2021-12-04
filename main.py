import pygame as pg
from Obstacles import *
from UI import *

WIDTH, HEIGHT = 800, 600
FPS = 120

BG = (25, 25, 112)
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

    def run(self):
        while True:
            self.create_menu()
            
            while self.in_menu:
                self.clock.tick(FPS)
                self.screen.fill(BG)
                pg.display.set_caption(str(int(self.clock.get_fps())))

                self.UI.update([self.in_game])
                self.UI.draw()
                
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        exit()

                pg.display.flip()
            
            for event in pg.event.get():
                    if event.type == pg.QUIT:
                        exit()

            pg.display.filip()
    
    def create_menu(self):
        self.UI.add_text(self.screen, BLACK, pg.Vector2(300, 200), 30, "Супер-пупер игра!")
        self.UI.add_button(self.screen, TEAL, BLACK, pg.Vector2(200, 400), 200, 40, 15, "Начать")


if __name__ == '__main__':
    app = App()
    app.run()
                