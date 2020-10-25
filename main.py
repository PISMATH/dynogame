import random
import pygame
import assets


WIDTH = 360
HEIGHT = 200
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sai game")
clock = pygame.time.Clock()


class DynoAsset(pygame.sprite.Sprite):
    image = None
    def draw_image(self, string):
        x, y = (0, 0)
        for row in string:
            for character in row:
                if character == "X":
                    self.image.set_at((x,y), BLACK)
                x += 1
            y += 1
            x = 0

# sprites
class Player(DynoAsset):
    y = 0
    def __init__(self):
        DynoAsset.__init__(self)
        self.image = pygame.Surface((20, 20), )
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.state = 1

        self.rect.center = (round(WIDTH/2), round(HEIGHT/2))
        self.frames = {
            1: assets.CATUS,
            2: assets.CATUS,
            0: assets.CATUS,
            3: assets.CATUS
        }

    def update(self):
        dino = self.frames[self.state]
        self.draw_image(dino)

    def kill_player(self):
        self.state = 0

class Bird(DynoAsset):

    x = 100
    def __init__(self):
        DynoAsset.__init__(self)

        self.state = 1
        self.image = pygame.Surface((20, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (round(WIDTH/2), round(HEIGHT/2))

    def update(self):
        self.x -= 1
        string = 1
        if self.state == 1:
            string = assets.BIRD_1
            self.state = 2
        elif self.state == 2:
            string = assets.BIRD_2
            self.state = 1


        self.draw_image(string)
def make_bird(all_sprites):
    a = random.randint(0 ,50)
    if a < 3:
        all_sprites.add(Bird())

def main():
    all_sprites = pygame.sprite.Group()
    player = Player()
    bird = Bird()
    bird.rect.x = 0
    bird.rect.y = 0
    all_sprites.add(player)
    all_sprites.add(bird)
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
        make_bird(all_sprites)

if __name__ == "__main__":
    main()
    pygame.quit()