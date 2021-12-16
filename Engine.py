import pygame as pg
from Obstacles import Enemy
from math import cos, sin, radians


class Engine:
    def __init__(self, WIDTH, HEIGHT, angle):
        """
        :param WIDTH, HEIGHT - высота и ширина экрана
        :param angle - угол, на который поворачивается плоскость экрана
        """

        self.WIDTH, self.HEIGHT = WIDTH, HEIGHT
        self.angle = radians(angle)

    def orthogonal_projection_edge(self, obj):
        """
        Функция проецирует трехмерные координаты на плоскость экрана

        :param obj - объект, у которого будут изменяться координаты
        """
        obj.projected_coords = []
        for i in obj.coords:
            obj.projected_coords.append([pg.Vector2(i.A.x , i.A.y*cos(self.angle) + i.A.z*sin(self.angle)), 
                                        pg.Vector2(i.B.x , i.B.y*cos(self.angle) + i.B.z*sin(self.angle)), 
                                        i.color, 
                                        i.thickness])
        
    def orthogonal_projection(self, obj):
        """
        Функция проецирует координаты центра объекта на плоскость экрана

        :param obj - объект, у которого будут изменяться координаты
        """
        obj.pos_center_v2 = pg.Vector2(obj.pos_center.x, obj.pos_center.y*cos(self.angle) + obj.pos_center.z*sin(self.angle))
    

if __name__ == '__main__':
    print('Не тот файл, надо запустить "main.py"')
