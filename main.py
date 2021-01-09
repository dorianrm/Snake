import pygame
from snake_class import Snake
from cube_class import Cube
# import math
# import random
# import tkinter as tk
# from tkinter import messagebox


'''
@param surface and its dimensions
Draws the grid portion of the game using lines
Lines = white
'''
def drawGrid(w, r, surface):
    sizeBtwn = w // r
    x, y = 0, 0
    for i in range(rows):
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
    global rows, width, s, snack
    surface.fill((0, 0, 0))  # color of background (black)
    drawGrid(width, rows, surface)
    s.draw(surface)
    snack.draw(surface)
    pygame.display.update()


'''
Controls running of game.
Only function called to play game
'''
def main():
    #global vars
    global width, rows, s, snack
    width, rows = 500, 20
    s = Snake('Red', (10,10))
    snack = Cube((0,0), 'Blue')

    #create window
    window = pygame.display.set_mode((width, width))

    flag = True
    clock = pygame.time.Clock()


    count = 0
    print('Just before while')
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        s.move()
        redrawWindow(window)
        count += 1
        # if count == 40:
        #     # flag = False
    pass

# --------------------
main()
