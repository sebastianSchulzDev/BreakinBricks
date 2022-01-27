import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Breakin' Bricks")

# bat
bat = pygame.image.load('./Images/paddle.png')
bat = bat.convert_alpha()
bat_rect = bat.get_rect()
bat_rect[1] = screen.get_height() - 100



# ball
ball = pygame.image.load('./Images/football.png')
ball = ball.convert_alpha()
ball_rect = ball.get_rect()
ball_start = ((screen.get_width() / 2), (screen.get_height() / 2))
ball_speed = (3.0, 3.0)
ball_served = False
sx, sy = ball_speed
ball_rect.topleft = ball_start

# brick
brick = pygame.image.load('./Images/brick.png')
brick = brick.convert_alpha()
brick_rect = brick.get_rect()
bricks = []
brick_rows = 5
brick_gap = 10
brick_cols = screen.get_width() // (brick_rect[2] + brick_gap)
side_gap = (screen.get_width() - (brick_rect[2] + brick_gap) * brick_cols + brick_gap) // 2

for y in range(brick_rows):
    brickY = y * (brick_rect[3] + brick_gap)
    for x in range(brick_cols):
        brickX = x * (brick_rect[2] + brick_gap) + side_gap
        bricks.append((brickX, brickY))


clock = pygame.time.Clock()
game_over = False
x = 0

while not game_over:
    dt = clock.tick(50)
    screen.fill((0, 0, 0))

    for b in bricks:
        screen.blit(brick, b)

    screen.blit(bat, bat_rect)
    screen.blit(ball, ball_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pressed = pygame.key.get_pressed()
    if pressed[K_RIGHT]:
        x += 0.5 * dt
    if pressed[K_LEFT]:
        x -= 0.5 * dt
    if pressed[K_SPACE]:
        ball_served = True

    if bat_rect[0] + bat_rect.width >= ball_rect[0] >= bat_rect[0] \
            and ball_rect[1] + bat_rect.height >= bat_rect[1] and sy > 0:
        sy *= -1
        sx *= 1.01 # speed increase
        sy *= 1.01 # speed increase
        continue

    delete_brick = None
    for b in bricks:
        bx, by = b
        if bx <= ball_rect[0] <= bx + brick_rect.width \
                and by <= ball_rect[1] <= by + brick_rect.height:
            delete_brick = b
            sy *= -1



    if delete_brick is not None:
        bricks.remove(delete_brick)

    # top
    if ball_rect[1] <= 0:
        ball_rect[1] = 0
        sy *= -1

    # bottom
    if ball_rect[1] >= screen.get_height() - ball_rect.height:
        # ball_rect[1] = screen.get_height() - ball_rect.height
        ball_rect[0], ball_rect[1] = ball_start[0], ball_start[1]
        ball_served = False

    # left
    if ball_rect[0] <= 0:
        ball_rect[0] = 0
        sx *= -1

    # right
    if ball_rect[0] >= screen.get_width() - ball_rect.width:
        ball_rect[0] = screen.get_width() - ball_rect.width
        sx *= -1

    bat_rect[0] = x

    if ball_served:
        ball_rect[0] += sx
        ball_rect[1] += sy
    pygame.display.update()
pygame.quit()
