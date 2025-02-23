import pygame

# pygame initialisation
pygame.init()

# constant width and height
WIDTH = 800
HEIGHT = 600

# setup of screen and title
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Boilerplate')

# clock setup
clock = pygame.time.Clock()

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()
