import pygame
from pygame.locals import *
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# game variables
score = 0
font = pygame.font.Font(None, 36)
game_over = False

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Circles')

# colours
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
bg_blue = (25, 30, 50)
grey = (98, 98, 98)


# background setup
def draw_bg():
    screen.fill(bg_blue)


def draw_dashed_line(surface, color, start_pos, end_pos, dash_length=10, gap_length=10):
    x = start_pos[0]
    y1, y2 = start_pos[1], end_pos[1]

    for y in range(y1, y2, dash_length + gap_length):
        pygame.draw.line(surface, color, (x, y), (x, min(y + dash_length, y2)))


def draw_score():
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))  # Draw in top-left corner


def draw_game_over():
    game_over_text = font.render("GAME OVER", True, (255, 0, 0))
    restart_text = font.render("Press 'R' to Restart", True, (255, 255, 255))

    screen.blit(game_over_text, (SCREEN_WIDTH //
                2 - 80, SCREEN_HEIGHT // 2 - 20))
    screen.blit(restart_text, (SCREEN_WIDTH //
                2 - 100, SCREEN_HEIGHT // 2 + 20))


def reset_game():
    global game_over, score
    game_over = False
    score = 0

    # Clear all sprites (bullets & balls)
    bullets.empty()
    balls.empty()

    # Reset player position
    character.rect.center = (SCREEN_WIDTH // 5, SCREEN_HEIGHT // 2)


# player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'circle_game_one_files/img/character.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.shoot_cooldown = 0  # Cooldown for shooting

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
            0, 0, SCREEN_WIDTH / 2, SCREEN_HEIGHT))

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

        # Check if space is held down & cooldown is 0, then shoot
        if key[pygame.K_SPACE] and self.shoot_cooldown == 0:
            self.shoot(bullets)
            self.shoot_cooldown = 20  # Set cooldown (adjust for fire rate)

    def shoot(self, bullet_group):
        bullet = Bullet(self.rect.centerx, self.rect.bottom)
        bullet_group.add(bullet)


# bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 4))  # Bullet size
        self.image.fill(grey)  # Red bullet
        self.rect = self.image.get_rect(center=(x + 15, y - 11))
        self.speed = -10

    def update(self):
        self.rect.x -= self.speed  # Move the bullet right
        if self.rect.left > SCREEN_WIDTH:  # Remove bullet if it goes off-screen
            self.kill()


# enemy class
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.radius = random.randint(15, 30)  # Random ball size
        self.image = pygame.Surface(
            (self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, 'white', (self.radius,
                           self.radius), self.radius)  # Draw red circle
        self.rect = self.image.get_rect()

        # Spawn on the right side at a random height
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(50, SCREEN_HEIGHT - 50 - self.radius * 2)

        self.speed = random.randint(1, 4)  # Random speed

    def update(self):
        self.rect.x -= self.speed  # Move left
        if self.rect.right < 0:  # Remove when off-screen
            self.kill()


# sprite groups
character_group = pygame.sprite.Group()
bullets = pygame.sprite.Group()
balls = pygame.sprite.Group()

character = Player(int(SCREEN_WIDTH / 5), SCREEN_HEIGHT / 2)
character_group.add(character)

BALL_SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(BALL_SPAWN_EVENT, 1000)

run = True
while run:
    clock.tick(fps)

    draw_bg()
    draw_score()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == BALL_SPAWN_EVENT:
            ball = Ball()
            balls.add(ball)
        if event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_r:  # Restart when "R" is pressed
                reset_game()

    if not game_over:
        character_group.update()
        bullets.update()
        balls.update()

        hits = pygame.sprite.groupcollide(bullets, balls, True, True)
        if hits:
            score += 1

        if pygame.sprite.spritecollide(character, balls, False):
            game_over = True

    character_group.draw(screen)
    bullets.draw(screen)
    balls.draw(screen)

    draw_dashed_line(screen, (255, 255, 255), (400, 0),
                     (400, 600), dash_length=1, gap_length=10)

    if game_over:
        draw_game_over()

    pygame.display.update()
    pygame.display.flip()

pygame.quit()
