# python3 -m venv venv
# source venv/bin/activate
# deactivate
import pygame
# import math
# import random
# import tkinter as tk
# from tkinter import messagebox
from snake_class import Snake

'''
@param surface and its dimensions
Draws the grid portion of the game using lines
Lines = white
'''


def drawGrid(w, rows, surface):
    sizeBtwn = w // rows
    x, y = 0, 0
    for i in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
        # row lines start pos, end pos of line
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))  # row lines
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))  # col lines


'''
@param surface aka window of game
Redraws game surface + elements (window, cubes, grid, snake) 
'''


def redrawWindow(surface):
    global rows, width, s, snack
    surface.fill((0, 0, 0))  # color of background (black)
    drawGrid(width, rows, surface)
    s.draw(surface)
    snake.draw(surface)
    pygame.display.update()


'''
Controls running of game.
Only function called to play game
'''


def main():
    # Initialize pygame module
    # pygame.init()

    # create window
    global width, rows, s, snack
    width, rows = 500, 20
    window = pygame.display.set_mode((width, width))

    flag = True
    clock = pygame.time.Clock()

    s = Snake('Red', 10)
    count = 0
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(window)
        s.sound()
        count += 1
        if count == 50:
            flag = False


# Run program
main()
