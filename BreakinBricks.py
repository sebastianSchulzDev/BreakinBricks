import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Breakin' Bricks")

#bat
bat = pygame.image.load('./Images/paddle.png')
bat = bat.convert_alpha()
bat_rect = bat.get_rect()

#ball
ball = pygame.image.load('./Images/football.png')
ball = ball.convert_alpha()
ball_rect = ball.get_rect()

#brick
brick = pygame.image.load('./Images/brick.png')
brick = brick.convert_alpha()
brick_rect = brick.get_rect()


clock = pygame.time.Clock()
game_over = False

while not game_over:
    dt = clock.tick(50)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

pygame.quit()
