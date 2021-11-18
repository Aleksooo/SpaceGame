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


def read_data(file) -> Edge:
    pass
