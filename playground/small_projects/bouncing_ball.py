import pygame
from pygame.locals import *

WIDTH = 1280
HEIGHT = 750
FPS = 60
SPEED = 600

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:

    screen.fill('purple')

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= SPEED * dt
    if keys[pygame.K_s]:
        player_pos.y += SPEED * dt
    if keys[pygame.K_a]:
        player_pos.x -= SPEED * dt
    if keys[pygame.K_d]:
        player_pos.x += SPEED * dt

    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
