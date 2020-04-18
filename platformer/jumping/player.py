import pygame

RED = (255, 0, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        width = 40
        height = 60
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)
 
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
 
        # Set speed vector of player
        self.velocity_y = 0
 
    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
 
        # Move up/down
        self.rect.y += self.velocity_y
 
 
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.velocity_y == 0:
            self.velocity_y = 1
        else:
            self.velocity_y += .35
 
        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.velocity_y >= 0:
            self.velocity_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
 
    def jump(self):
        self.velocity_y = -10

    def go_left(self):
        if self.rect.x > 0:
            self.rect.x += -6
 
    def go_right(self):
        if self.rect.x < 760:
            self.rect.x += 6
 