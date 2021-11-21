import pygame as pg
from Obstacles import *

WIDTH, HEIGHT = 800, 600
FPS = 60

BG = (25, 25, 112)


class App:
    def __init__(self):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()

    def run(self):
        while True:
            self.clock.tick(FPS)
            self.screen.fill(BG)
            pg.display.set_caption(str(int(self.clock.get_fps())))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()

            pg.display.flip()


if __name__ == '__main__':
    app = App()
    app.run()
                