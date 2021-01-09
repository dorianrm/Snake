import pygame
from cube_class import Cube
import settings 
class Snake(object):
    body = [] #List of cubes
    turns = {}
    
    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dir_x = 0
        self.dir_y = 0
        rows = settings.rows

    def sound(self):
        print("hissss")

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_a]:
                    self.dir_x = -1
                    self.dir_y = 0
                    self.turns[self.head.pos[:]] = [self.dir_x, self.dir_y]
                elif keys[pygame.K_d]:
                    self.dir_x = 1
                    self.dir_y = 0
                    self.turns[self.head.pos[:]] = [self.dir_x, self.dir_y]
                elif keys[pygame.K_w]:
                    self.dir_x = 0
                    self.dir_y = -1
                    self.turns[self.head.pos[:]] = [self.dir_x, self.dir_y]
                elif keys[pygame.K_s]:
                    self.dir_x = 0
                    self.dir_y = 1
                    self.turns[self.head.pos[:]] = [self.dir_x, self.dir_y]

        for i, block in enumerate(self.body):
            p = block.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                block.move(turn[0], turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            
            else:
                if block.dir_x == -1 and block.pos[0] <= 0: #left
                    block.pos = (block.rows-1, block.pos[1])
                elif block.dir_x == 1 and block.pos[0] >= block.rows-1: #right
                    block.pos = (0, block.pos[1])
                elif block.dir_y == 1 and block.pos[1] >= block.rows-1:
                    block.pos = (block.pos[0], 0)
                else:
                    block.move(block.dir_x, block.dir_y)

    
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
            if i == 0: #head = eyes
                block.draw(surface, True) 
            else: #body
                block.draw(surface)

    def reset(self, pos):
        self.head = Cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dir_x = 0
        self.dir_y = 1   

