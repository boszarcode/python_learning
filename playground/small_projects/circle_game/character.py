import pygame
from screen_variables import *


vector = pygame.Vector2


class Character(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'circle_game/img/character.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        speed = 20

        key = pygame.key.get_pressed()
        up = key[pygame.K_w]
        down = key[pygame.K_s]
        left = key[pygame.K_a]
        right = key[pygame.K_d]

        move = pygame.math.Vector2(right - left, down - up)
        if move.length_squared() > 0:
            move.scale_to_length(speed)
            self.rect.move_ip(round(move.x), round(move.y))
        self.rect.clamp_ip(pygame.Rect(
            0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
