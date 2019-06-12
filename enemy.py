import pygame
import random
import settings as st

class SEnemy(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        #存活画面
        self.image = pygame.image.load(st.small_enemy)

        #毁灭画面
        self.d_image = []
        self.d_image.extend([\
            pygame.image.load(st.small_enemy_destroy_1),\
            pygame.image.load(st.small_enemy_destroy_2),\
            pygame.image.load(st.small_enemy_destroy_3),\
            pygame.image.load(st.small_enemy_destroy_4)\
            ])
        
        self.rect = self.image.get_rect()
        self.width = bg_size[0]
        self.height = bg_size[1]
        self.rect.left = random.randint(0, self.width - 57)
        self.rect.bottom = 0
        self.speed = 4

        self.mask = pygame.mask.from_surface(self.image)

        #检测飞机存活状态
        self.alive = True

    def move(self):
        self.rect.bottom += self.speed

        if self.rect.top == self.height:
            self.kill()


class MEnemy(SEnemy):
    hp = 3
    def __init__(self, bg_size):
        SEnemy.__init__(self, bg_size)

        #存活画面
        image = st.normal_enemy
        self.image = pygame.image.load(image)

        #毁灭画面
        self.d_image = []
        self.d_image.extend([\
            pygame.image.load(st.normal_enemy_destroy_1),\
            pygame.image.load(st.normal_enemy_destroy_2),\
            pygame.image.load(st.normal_enemy_destroy_3),\
            pygame.image.load(st.normal_enemy_destroy_4)\
            ])

        
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(0, self.width - 70)
        self.rect.bottom = 0
        self.speed = 2

        #生命值
        self.hp =MEnemy.hp

        self.mask = pygame.mask.from_surface(self.image)


class BEnemy(SEnemy):
    hp = 5
    def __init__(self, bg_size):
        SEnemy.__init__(self, bg_size)
        #存活画面
        image_1 = st.big_enemy_one
        image_2 = st.big_enemy_two

        #毁灭画面
        self.d_image = []
        self.d_image.extend([\
            pygame.image.load(st.big_enemy_destroy_1),\
            pygame.image.load(st.big_enemy_destroy_2),\
            pygame.image.load(st.big_enemy_destroy_3),\
            pygame.image.load(st.big_enemy_destroy_4),\
            pygame.image.load(st.big_enemy_destroy_5),\
            pygame.image.load(st.big_enemy_destroy_6)\
            ])
        
        self.image_1 = pygame.image.load(image_1)
        self.image_2 = pygame.image.load(image_2)
        self.rect = self.image_1.get_rect()
        self.rect.left = random.randint(0, self.width - 180)
        self.rect.bottom = 0
        self.speed = 1

        #生命值
        self.hp = BEnemy.hp

        self.mask = pygame.mask.from_surface(self.image_1)
