import pygame
import settings as st
from snake_class import Snake
from cube_class import Cube

import random
import math
import tkinter as tk
from tkinter import messagebox


def randomSnack(rows, item):

    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            # found (x,y) snack that's not in snake body
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
        pygame.draw.line(surface, st.grid_color, (x, 0), (x, w))  # row lines
        pygame.draw.line(surface, st.grid_color, (0, y), (w, y))  # col lines


'''
@param surface aka window of game
Redraws game surface + elements (window, grid, cubes, snake) 
'''
def redrawWindow(surface):
    global s, snack
    surface.fill((0, 0, 0))  # color of background (black)
    drawGrid(st.width, st.rows, surface)
    s.draw(surface)
    snack.draw(surface)
    pygame.display.update()

def snack_check():
    global s, snack
    if s.body[0].pos == snack.pos:
        s.addCube()
        snack = Cube(randomSnack(st.rows, s), color=st.snack_color)

# def snake_check():
#     global s

def message_box(subject, content):
    # tcl = tk.Tcl()
    # print(tcl.call("info", "patchlevel"))
    print('START OF MESSAGE_BOX')
    root = tk.Tk()
    print('AFTER CALL TO ROOT')
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

'''
Controls running of game.
Only function called to play game
'''
def main():
    #global vars
    global s, snack
    st.init()
    s = Snake(st.snake_color, (st.snake_x, st.snake_y))
    snack = Cube(randomSnack(st.rows, s), color=st.snack_color)

    #create window
    window = pygame.display.set_mode((st.width, st.width))

    #Display elements
    flag = True
    clock = pygame.time.Clock()
    delay_time = 50
    tick_time = 10

    while flag:
        pygame.time.delay(delay_time)
        clock.tick(tick_time)
        s.move()
        snack_check()
        # snake_check()
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
                print('Score: ', len(s.body))
                # message_box('You Lost!', 'Play again...')
                s.reset((10,10))
                break
        redrawWindow(window)
    pass

# ----------------------------------
main()
