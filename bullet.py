import pygame
import settings as st


class Bullet(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        #子弹图片
        # image = st.normal_bullet
        # image_super = st.super_bullet
        self.image = pygame.image.load(st.normal_bullet).convert_alpha()
        self.image_super = pygame.image.load(st.super_bullet).convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.left = position[0] 
        self.rect.bottom = position[1]

        self.speed = 14
        self.mask = pygame.mask.from_surface(self.image)
        self.alive = True

    def moveup(self):
        self.rect.bottom -= self.speed
        if self.rect.bottom == 0:
            self.kill()
