import random
import pygame
import os

WIDTH = 360
HEIGHT = 480
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sai game")
clock = pygame.time.Clock()
# sprites
class Player(pygame.sprite.Sprite ):
    y = 0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("d.png")
        self.rect = self.image.get_rect()
        self.rect.center = (round(WIDTH/2), round(HEIGHT/2))

    def update(self):



all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(Player)
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update
    all_sprites.update()
    #  Draw / render
    all_sprites.draw(screen)
    screen.fill(WHITE)
    pygame.display.flip()
pygame.quit()