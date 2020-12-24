import pygame
from cube_class import Cube 
class Snake(object):
    body = [] #List of cubes
    def __init__(self, color, pos):
        self.color = color
        self.head = pos
        self.body.append(self.head)
        self.dir_x = 0
        self.dir_y = 0

    def sound(self):
        print("hissss")

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dir_x = -1
                    self.dir_y = 0
                elif keys[pygame.K_RIGHT]:
                    self.dir_x = 1
                    self.dir_y = 0
                elif keys[pygame.K_UP]:
                    self.dir_x = 0
                    self.dir_y = -1
                elif keys[pygame.K_DOWN]:
                    self.dir_x = 0
                    self.dir_y = 1
    
    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dir_x, tail.dir_y

        if dx == 1 and dy == 0: # moving right
            new_pos = (tail.pos[0]-1, tail.pos[1])
            self.body.append(Cube(new_pos))
        elif dx == -1 and dy == 0: # left
            new_pos = (tail.pos[0]+1, tail.pos[1])
            self.body.append(Cube(new_pos))
        elif dx == 0 and dy == -1: # up
            new_pos = (tail.pos[0], tail.pos[1]+1)
            self.body.append(Cube(new_pos))
        elif dx == 0 and dy == 1: # down
            new_pos = (tail.pos[0], tail.pos[1]-1)
            self.body.append(Cube(new_pos))

        self.body[-1].dir_x = dx
        self.body[-1].dir_y = dy   

    def draw(self, surface):
        for i,block in enumerate(self.body):
            if i == 0:
                block.draw(surface, True) 
            else:
                block.draw(surface)   

