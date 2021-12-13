from Edge import *
from random import randint
from math import log, cosh, sqrt


def f(x, h, b):
    a = -log((h+1)/b+sqrt((h+1)**2/b**2 - 1))/400
    return -(b*cosh(a*(x-400))-1)


class Terrain():
    def __init__(self, screen, width, height, num_x, num_z, lift, color, thickness):
        self.screen = screen
        self.width = width
        self.height = height
        self.num_x = num_x
        self.num_z = num_z
        self.lift = lift
        self.color = color
        self.thickness = thickness

        self.vertexes = []
        self.coords = []
        self.projected_coords = []

        self.dx = self.width/self.num_x
        self.dz = self.height/self.num_z
        self.dy = 6
        self.h = 50
        self.b = 0.01

        self.time = 0
        self.delay = 5

        self.generate_terrain()

    def generate_terrain(self):
        for x in range(0, self.num_x+1):
            self.vertexes.append([])
            for z in range(0, self.num_z+1):
                self.vertexes[x].append(pg.Vector3(self.dx*x, f(x*self.dx, self.h, self.b) + randint(-self.dy, self.dy), self.dz*z))
    '''
    def noise(self):
        for x in range(0, self.num_x+1):
            for z in range(0, self.num_z+1):
                self.vertexes[x][z].y += randint(-abs(x-self.num_x/2), abs(x-self.num_x/2))
    '''            
    def move(self):
        for x in range(0, self.num_x+1):
            self.vertexes[x][-1].y = f(x*self.dx, self.h, self.b) + randint(-self.dy, self.dy)
            for z in range(0, self.num_z):
                self.vertexes[x][z].y = self.vertexes[x][z+1].y

            self.vertexes[x][-1].y = f(x*self.dx, self.h, self.b) + randint(-self.dy, self.dy)

    def update(self) -> None:
        if self.time == self.delay:
            self.move()
            self.time = 0
        self.time += 1

        self.coords = []
        for x in range(0, self.num_x+1):
            for z in range(0, self.num_z+1):
                if x != self.num_x:
                    # горизонтальная линия
                    self.coords.append(Edge(self.vertexes[x][z], self.vertexes[x+1][z], 
                                       self.color, self.thickness))
                if z != self.num_z:
                    # вертикальная линия
                    self.coords.append(Edge(self.vertexes[x][z], self.vertexes[x][z+1], 
                                        self.color, self.thickness))
    
    def draw(self):
        pos_center_v2 = pg.Vector2(0, self.lift)
        for i in self.projected_coords:
            pg.draw.line(self.screen, i[2], pos_center_v2 + i[0], pos_center_v2 + i[1], i[3])


if __name__ == '__main__':
    print('Не тот файл, надо запустить "main.py"')
