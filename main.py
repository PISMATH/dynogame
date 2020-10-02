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
class Player(pygame.sprite.Sprite):
    y = 0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20), )
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

        self.rect.center = (round(WIDTH/2), round(HEIGHT/2))

    def update(self):
        self.draw_image(DINO)

    def draw_image(self, string):
        x, y = (0, 0)
        for row in string:
            for character in row:
                if character == "X":
                    self.image.set_at((x,y),BLACK)
                x += 1
            y += 1
            x = 0


DINO = [
    #01234567890123456789
    "____________________",  # 0
    "___________XXXXXX___",  # 1
    "__________XXXXXXXX__",  # 2
    "__________XX_XXXXX__",  # 3
    "__________XXXXXXXXX_",  # 4
    "__________XXXX______",  # 5
    "__________XXXXXXXX__",  # 6
    "__________XXX_______",  # 7
    "_________XXXX_______",  # 8
    "X________XXXXXXXX___",  # 9
    "X_______XXXXXX__X___",  # 10
    "XX_____XXXXXXX______",  # 11
    "_XX___XXXXXXXX______",  # 12
    "__XXXXXXXXXXX_______",  # 13
    "____XXXXXXXX________",  # 14
    "_____XXXXXX_________",  # 15
    "_____XXX_XX_________",  # 16
    "_____XX___X_________",  # 17
    "_____X____X_________",  # 18
    "_____XX___XX________",  # 19
    "____________________",  # 20
]
CATUS = [
    "__XX__",
    "X_XX_X",
    "XXXXXX",
    "__XX__",
    "__XX__",
    "__XX__",
]
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update
    all_sprites.update()
    #  Draw / render
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()