import pygame
import settings
from snake_class import Snake
from cube_class import Cube

import random
# import math
# import tkinter as tk
# from tkinter import messagebox


def randomSnack(rows, item):

    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            break

    return (x,y)

'''
@param surface and its dimensions
Draws the grid portion of the game using lines
Lines = white
'''
def drawGrid(w, r, surface):
    sizeBtwn = w // r
    x, y = 0, 0
    for i in range(r):
        x = x + sizeBtwn
        y = y + sizeBtwn
        # row lines start pos, end pos of line
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))  # row lines
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))  # col lines


'''
@param surface aka window of game
Redraws game surface + elements (window, grid, cubes, snake) 
'''
def redrawWindow(surface):
    global s, snack
    surface.fill((0, 0, 0))  # color of background (black)
    drawGrid(settings.width, settings.rows, surface)
    s.draw(surface)
    snack.draw(surface)
    pygame.display.update()


'''
Controls running of game.
Only function called to play game
'''
def main():
    print('START OF MAIN')
    #global vars
    # global width, rows, s, snack
    # width, rows = 500, 20
    global s, snack
    settings.init()
    s = Snake('Red', (10,10))
    snack = Cube((0,0), 'Blue')

    #create window
    window = pygame.display.set_mode((settings.width, settings.width))

    #Display elements
    flag = True
    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        s.move()
        redrawWindow(window)
    pass

# --------------------
main()
