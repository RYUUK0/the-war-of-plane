import pygame
import random
import settings as st



class Recruit(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image_1 = pygame.image.load(st.bomb_supply)
        self.image_2 = pygame.image.load(st.bullet_supply)

        self.width = bg_size[0]
        self.height = bg_size[1]
        self.rect = self.image_1.get_rect()
        self.rect.left = random.randint(0, bg_size[0] - self.rect.width)
        self.rect.bottom = 0

        self.speed = 6
        self.mask = pygame.mask.from_surface(self.image_1)
        self.alive = True

    def move(self):
        self.rect.bottom += self.speed

        if self.rect.top >= self.height:
            self.alive = False
            self.kill() 
        
        
