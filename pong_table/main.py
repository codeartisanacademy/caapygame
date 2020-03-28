import pygame

pygame.init()

screen = pygame.display.set_mode((700, 500))

clock = pygame.time.Clock()

carry_on = True

while carry_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carry_on = False

    screen.fill((0, 0, 0))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()