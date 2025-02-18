import pygame
from pygame.locals import *
import random
import character as char
from screen_variables import *

pygame.init()

# fps
clock = pygame.time.Clock()
fps = 60


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Circles')

# colours
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
bg_blue = (25, 30, 50)


# function for background


def draw_bg():
    screen.fill(bg_blue)


character_group = pygame.sprite.Group()

character = char.Character(int(SCREEN_WIDTH/2), SCREEN_HEIGHT - 100)
character_group.add(character)

run = True
while run:

    clock.tick(fps)

    # draw background
    draw_bg()

    # update
    character_group.update()

    # draw sprite groups
    character_group.draw(screen)

    # event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
