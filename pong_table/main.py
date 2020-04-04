import pygame
from paddle import Paddle
from ball import Ball

pygame.init()

screen = pygame.display.set_mode((700, 500))

WHITE = (255, 255, 255)
paddle = Paddle(WHITE, 100, 10)
paddle.x = 350
paddle.rect.y = 450

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

sprites_list = pygame.sprite.Group()
sprites_list.add(paddle)
sprites_list.add(ball)

clock = pygame.time.Clock()

carry_on = True

while carry_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carry_on = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move_left(5)
    if keys[pygame.K_RIGHT]:
        paddle.move_right(5)

    sprites_list.update()

    # if ball touch right wall
    if ball.rect.x >= 690:
        ball.velocity[0] = -ball.velocity[0]

    # if ball touch left wall
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    
    # if ball touch bottom wall
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    
    # if ball touch top wall
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    screen.fill((0, 0, 0))

    sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()