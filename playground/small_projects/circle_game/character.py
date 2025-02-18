import pygame
from screen_variables import *


class Character(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            '/Users/joemorris/repos/python_learning/playground/small_projects/circle_game/character.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        speed = 8

        key = pygame.key.get_pressed()
        if key[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= speed
        if key[pygame.K_d] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += speed
        if key[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= speed
        if key[pygame.K_s] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += speed
