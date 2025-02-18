import pygame
from pygame.locals import *

# define fps
clock = pygame.time.Clock()
fps = 60

screen_width = 600
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Game')


# load image
# bg = pygame.image.load(
#     "insert background image here")

# bg = pygame.transform.scale(bg, (600, 800))


run = True
while run:

    clock.tick(fps)

    # events handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update screen
    pygame.display.update()

pygame.quit()
