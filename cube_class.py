import pygame

class Cube(object):
    rows = 20 # UPDATE FROM main.py
    width = 500
    def __init__(self, pos, color=(255,0,0), dir_x=1, dir_y=0):
        self.pos = pos #tuple (x,y)
        self.color = color
        self.dir_x = 1
        self.dir_y = 0

    def move(self, dir_x, dir_y):
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.pos = (self.pos[0] + self.dir_x, self.pos[1] + self.dir_y)

    def draw(self, surface, eyes=False):
        dis = self.width // self.rows
        i,j = self.pos[0], self.pos[1]
        pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis-2))
        # rect(left_x, left_y, dim_x, dim_y)