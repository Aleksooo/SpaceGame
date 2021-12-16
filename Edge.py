import pygame as pg


class Edge:
    def __init__(self, pos_A, pos_B, color, thickness):
        """
        :param pos_A, pos_B - координы начала и конца грани
        :param color - цвет грани
        :param thickness - толщина линии
        """
        
        self.A = pos_A
        self.B = pos_B
        self.color = color
        self.thickness = thickness


def read_data(file):
    """
    Функция считывает из файла координаты вершин объектов для последующей отрисовки, возвращает массив элементов
    класса Edge

    :param file - файл, содержащий координатыЫ
    """
    coords = []
    with open(file) as file:
        for line in file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue

            parameters = line.split()
            for i in range(0, 3):
                parameters[i] = list(map(float, list(parameters[i].split(','))))

            parameters[0] = pg.Vector3(parameters[0])
            parameters[1] = pg.Vector3(parameters[1])
            parameters[3] = int(parameters[3])
            coords.append(Edge(parameters[0], parameters[1], parameters[2], parameters[3]))
    return coords

