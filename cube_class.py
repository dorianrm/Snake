import pygame

class Cube(object):

    def __init__(self, color=(255,0,0), pos, dir_x=1, dir_y=0):
        self.color = color
        self.pos = pos #tuple (x,y)
        self.dir_x = 1
        self.dir_y = 0

    def move(self, dir_x, dir_y):
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.pos = (self.pos[0] + self.dir_x, self.pos[1] + self.dir_y)
