import pygame
from pygame import mixer
from pygame.locals import *
import random

pygame.init()

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
volume = 0.25

# define fps
clock = pygame.time.Clock()
fps = 60

screen_width = 600
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invaders')

# define fonts
font30 = pygame.font.SysFont('Futura', 30)
font40 = pygame.font.SysFont('Futura', 40)

# load sounds
explosion_fx = pygame.mixer.Sound(
    "/Users/joemorris/repos/python_learning/playground/small_projects/img/explosion.wav")
explosion_fx.set_volume(volume)

explosion2_fx = pygame.mixer.Sound(
    "/Users/joemorris/repos/python_learning/playground/small_projects/img/explosion2.wav")
explosion2_fx.set_volume(1)

laser_fx = pygame.mixer.Sound(
    "/Users/joemorris/repos/python_learning/playground/small_projects/img/laser.wav")
laser_fx.set_volume(volume)

# define game variables
rows = 5
cols = 5
last_alien_shot = pygame.time.get_ticks()
alien_cooldown = 1000  # ms
countdown = 3
last_count = pygame.time.get_ticks()
game_over = 0  # 0 is no game over, 1 is player won, -1 is player lost

# define colours
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)


def draw_bg():
    # screen.blit(bg, (0, 0))
    screen.fill(black)

# define function for creatin text


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# create spaceship class


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            '/Users/joemorris/repos/python_learning/playground/small_projects/img/spaceship.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.health_start = health
        self.health_remaining = health
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        # set movement speed
        speed = 8

        game_over = 0

        # set cooldown variable (ms)
        cooldown = 80

        # get key press
        key = pygame.key.get_pressed()
        if key[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= speed
        if key[pygame.K_d] and self.rect.right < screen_width:
            self.rect.x += speed
        if key[pygame.K_w] and self.rect.top > 600:
            self.rect.y -= speed
        if key[pygame.K_s] and self.rect.bottom < screen_height - 50:
            self.rect.y += speed

        # record current time
        time_now = pygame.time.get_ticks()

        # shooting
        if key[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
            laser_fx.play()
            bullet = Bullets(self.rect.centerx, self.rect.top)
            bullet_group.add(bullet)
            self.last_shot = time_now

        # update mask
        self.mask = pygame.mask.from_surface(self.image)

        # draw health bar
        pygame.draw.rect(
            screen, red, (self.rect.x, (self.rect.bottom + 10),
                          self.rect.width, 15))
        if self.health_remaining > 0:
            pygame.draw.rect(screen, green, (self.rect.x, (self.rect.bottom + 10), int(
                self.rect.width * (self.health_remaining / self.health_start)), 15))
        elif self.health_remaining <= 0:
            explosion = Explosion(self.rect.centerx, self.rect.centery, 3)
            explosion_group.add(explosion)
            self.kill()
            game_over = -1
        return game_over

        # create bullet class


class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            '/Users/joemorris/repos/python_learning/playground/small_projects/img/bullet.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()
        if pygame.sprite.spritecollide(self, alien_group, True):
            self.kill()
            explosion_fx.play()
            explosion = Explosion(self.rect.centerx, self.rect.centery, 2)
            explosion_group.add(explosion)


# create aliens class

class Aliens(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            '/Users/joemorris/repos/python_learning/playground/small_projects/img/alien' + str(random.randint(1, 5)) + '.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.move_counter = 0
        self.move_direction = 1

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 75:
            self.move_direction *= -1
            self.move_counter *= self.move_direction

# create alien bullets


class Alien_Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            '/Users/joemorris/repos/python_learning/playground/small_projects/img/alien_bullet.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y += 2
        if self.rect.top > screen_height:
            self.kill()
        if pygame.sprite.spritecollide(self, spaceship_group, False, pygame.sprite.collide_mask):
            self.kill()
            explosion2_fx.play()
            # reduce spaceship health
            spaceship.health_remaining -= 1
            explosion = Explosion(self.rect.centerx, self.rect.centery, 1)
            explosion_group.add(explosion)

# create explosion class


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 6):
            img = pygame.image.load(
                f"/Users/joemorris/repos/python_learning/playground/small_projects/img/exp{num}.png")
            if size == 1:
                img = pygame.transform.scale(img, (20, 20))
            if size == 2:
                img = pygame.transform.scale(img, (40, 40))
            if size == 3:
                img = pygame.transform.scale(img, (100, 100))
            # add image to the list
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0

    def update(self):
        explosion_speed = 3
        # update explosion animation
        self.counter += 1

        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        # if animation complete, delete explosion
        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()


# create sprite group
spaceship_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()
alien_bullet_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()


def create_aliens():
    # generate aliens
    for row in range(rows):
        for item in range(cols):
            alien = Aliens(100 + item * 100, 100 + row * 70)
            alien_group.add(alien)


create_aliens()


# create player
spaceship = Spaceship(
    int(screen_width / 2), screen_height - 100, 3)
spaceship_group.add(spaceship)

run = True
while run:

    clock.tick(fps)

    # draw background
    draw_bg()

    if countdown == 0:

        # create random alien bullets
        # record current time
        time_now = pygame.time.get_ticks()
        # shoot
        if time_now - last_alien_shot > alien_cooldown and len(alien_bullet_group) < 5:
            attacking_alien = random.choice(alien_group.sprites())
            alien_bullet = Alien_Bullets(
                attacking_alien.rect.centerx, attacking_alien.rect.bottom)
            alien_bullet_group.add(alien_bullet)
            last_alien_shot = time_now

        # check if all aliens have been killed
        if len(alien_group) == 0:
            game_over = 1

        if game_over == 0:
            # update spaceship
            game_over = spaceship.update()

            # update sprite group
            bullet_group.update()
            alien_group.update()
            alien_bullet_group.update()
        else:
            if game_over == -1:
                draw_text("GAME OVER!", font40, white, int(
                    screen_width / 2 - 110), int(screen_height / 2 + 50))
            if game_over == 1:
                draw_text("YOU WIN!", font40, white, int(
                    screen_width / 2 - 110), int(screen_height / 2 + 50))

    if countdown > 0:
        draw_text("GET READY!", font40, white, int(
            screen_width / 2 - 110), int(screen_height / 2 + 50))
        draw_text(str(countdown), font40, white, int(
            screen_width / 2 - 10), int(screen_height / 2 + 100))
        count_timer = pygame.time.get_ticks()
        if count_timer - last_count > 1000:
            countdown -= 1
            last_count = count_timer

    # explosion update group
    explosion_group.update()

    # draw sprite groups
    spaceship_group.draw(screen)
    bullet_group.draw(screen)
    alien_group.draw(screen)
    alien_bullet_group.draw(screen)
    explosion_group.draw(screen)

    # events handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update screen
    pygame.display.update()

pygame.quit()
