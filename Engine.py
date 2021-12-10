import pygame as pg
from Obstacles import Enemy
from math import cos, sin, radians


class Engine:
    def __init__(self, WIDTH, HEIGHT, angle):
        """
        :param WIDTH, HEIGHT - высота и ширина экрана
        """

        self.WIDTH, self.HEIGHT = WIDTH, HEIGHT
        self.angle = radians(angle)
    '''
    def add_element(self, element):
        self.all_elements.append(element)
    '''
    def update(self):
        pass

    def rotate_plane(self, ax: str, ange: float):
        pass

    def orthogonal_projection(self, obj) -> list:
        obj.projected_coords = []
        for i in obj.coords:
            obj.projected_coords.append([pg.Vector2(i.A.x , i.A.y*cos(self.angle) + i.A.z*sin(self.angle)), 
                                        pg.Vector2(i.B.x , i.B.y*cos(self.angle) + i.B.z*sin(self.angle)), 
                                        i.color, 
                                        i.thickness])
    

if __name__ == '__main__':
    print('Не тот файл, надо запустить "main.py"')
