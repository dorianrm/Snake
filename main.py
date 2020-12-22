# python3 -m venv venv
# source venv/bin/activate
# deactivate
import pygame
# import math
# import random
# import tkinter as tk
# from tkinter import messagebox
from snake_class import Snake


def drawGrid(w, rows, surface):
    sizeBtwn = w // rows
    x = 0
    y = 0
    for i in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
        # row lines start pos, end pos of line
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))  # col lines


def redrawWindow(surface):
    global rows, width
    surface.fill((0, 0, 0))
    drawGrid(width, rows, surface)
    pygame.display.update()


def main():
    # Initialize pygame module
    # pygame.init()

    # create window
    global width, rows
    width = 500
    rows = 20
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
        if count == 20:
            flag = False


main()
