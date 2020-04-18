import pygame
from player import Player

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)

pygame.init()
 
# Set the height and width of the screen
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
 
player = Player()

active_sprite_list = pygame.sprite.Group()
player.rect.x = 340
player.rect.y = SCREEN_HEIGHT - player.rect.height
active_sprite_list.add(player)

done = False

clock = pygame.time.Clock()

while not done:
    print("\n=======\ny pos %d, y vel %d\n=======\n" % (player.rect.y, player.velocity_y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            player.jump()
                

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.go_left()
    if keys[pygame.K_RIGHT]:
        player.go_right()
    
    # pygame.time.wait(50)
    screen.fill(BLACK)
    active_sprite_list.update()
    active_sprite_list.draw(screen)
    clock.tick(60)
    pygame.display.flip()

pygame.quit()