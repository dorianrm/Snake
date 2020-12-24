import pygame
pygame.init()
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

    def draw(self, surface):
        pass
        # for i,c in enumerate(self.body):
        #     if i == 0:
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

