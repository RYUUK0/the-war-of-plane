import pygame
import settings as st


#定义飞机类，需要边界范围
class Plane(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        #存活画面
        self.image_1 = pygame.image.load(st.me_1).convert_alpha()
        self.image_2 = pygame.image.load(st.me_2).convert_alpha()

        #毁灭画面
        self.d_image = []
        self.d_image.extend([\
            pygame.image.load(st.me_destroy_1),\
            pygame.image.load(st.me_destroy_2),\
            pygame.image.load(st.me_destroy_3),\
            pygame.image.load(st.me_destroy_4)\
            ])
        
        
        self.rect = self.image_1.get_rect()
        self.width = bg_size[0]
        self.height = bg_size[1]
        self.rect.left = self.width // 2
        self.rect.top = self.height - self.rect.height
        self.speed = 10

        self.mask = pygame.mask.from_surface(self.image_1)

        #飞机存活状态
        self.alive = True
        

    def moveleft(self):
        self.rect.left -= self.speed
        if self.rect.left < 0:
            self.rect.left = 0
            
            
    def moveright(self):
        self.rect.right += self.speed
        if self.rect.right > self.width:
            self.rect.right = self.width

            
    def movedown(self):
        self.rect.bottom += self.speed
        if self.rect.bottom > self.height:
            self.rect.bottom = self.height 
            
    def moveup(self):
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.rect.top = 0
