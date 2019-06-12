import pygame
import sys
import traceback


import plane
import enemy
import bullet
import recruit
import settings as st

import random
from pygame.locals import *

#初始化
pygame.init()

#颜色
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)


#加载背景
bg = pygame.image.load(st.background)
bg_rect = bg.get_rect()
bg_size = bg_rect.width, bg_rect.height

#建立窗口
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption('飞机大战')




#建立敌人刷新事件(小飞机)
ADD_SE = pygame.USEREVENT
pygame.time.set_timer(ADD_SE, 1000)

#建立中型飞机
ADD_ME = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ME, 2500)


#建立大型飞机
ADD_BE = pygame.USEREVENT + 2
pygame.time.set_timer(ADD_BE, 5000)


#建立子弹事件
EMIT = pygame.USEREVENT + 3
pygame.time.set_timer(EMIT, 400)



#建立补给刷新事件
ADD_RE = pygame.USEREVENT + 4
pygame.time.set_timer(ADD_RE, 10000)



def main():

    running = True


    #敌人和主角索引（毁灭播放）
    enemy_index = 0
    
    b_enemy_index = 0
    my_plane_index = 0

    
    #建立一个主角飞机
    me = plane.Plane(bg_size)
    clock = pygame.time.Clock()

    #刷新状态
    judge_num = 100
    switch_plane = True

    #建立小型飞机敌人列表
    s_enemys = pygame.sprite.Group()

    #建立中型飞机列表
    m_enemys = pygame.sprite.Group()
    
    #大型飞机列表
    b_enemys = pygame.sprite.Group()
    
    all_enemys = pygame.sprite.Group()

    #总分数
    all_grade = 0
    grade_font = pygame.font.Font('font\\font.ttf', 36)

    #建立补给列表
    bomb_rec = pygame.sprite.Group()
    super_rec = pygame.sprite.Group()
    all_rec = pygame.sprite.Group()

    #建立子弹列表
    bullets = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group()

    #炸弹数目
    bomb_num = 3

    #加载炸弹图片
    bomb_image = pygame.image.load(st.bomb)
    bomb_font = pygame.font.Font(st.grade_font, 48)

    

    #判断子弹类型
    is_super = False

    
    while running:
        screen.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            #触发对应事件（小中大飞机出现）
            if event.type == ADD_SE:
                new_s_enemy = enemy.SEnemy(bg_size)
                s_enemys.add(new_s_enemy)
                all_enemys.add(new_s_enemy)

            if event.type == ADD_ME:
                new_m_enemy = enemy.MEnemy(bg_size)
                m_enemys.add(new_m_enemy)
                all_enemys.add(new_m_enemy)

            if event.type == ADD_BE:
                new_b_enemy = enemy.BEnemy(bg_size)
                b_enemys.add(new_b_enemy)
                all_enemys.add(new_b_enemy)

            #子弹事件
            if event.type == EMIT:
                if not is_super:
                    new_bullet = bullet.Bullet(me.rect.midtop)
                    bullets.add(new_bullet)
                else:
                    super_bullet_1 = bullet.Bullet((me.rect.midtop[0] - 35, me.rect.bottom + me.rect.height / 2))
                    super_bullet_2 = bullet.Bullet((me.rect.midtop[0] + 25, me.rect.bottom + me.rect.height / 2))
                    bullets.add(super_bullet_1)
                    bullets.add(super_bullet_2)

            #补给事件
            if event.type == ADD_RE:
                rec_type  = random.choice([True, False])
                if rec_type:
                    new_bomb = recruit.Recruit(bg_size)
                    bomb_rec.add(new_bomb)
                else:
                    new_super_rec = recruit.Recruit(bg_size)
                    super_rec.add(new_super_rec)
                

            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    if bomb_num > 0:
                        bomb_num -= 1
                        for e in all_enemys:
                            e.alive = False
                            if e in s_enemys:
                                all_grade += 3000
                            if e in m_enemys:
                                all_grade += 6000
                            else:
                                all_grade += 12000
                
                

        #整个键盘序列，当被按下时，Bool为真
        key_pressed = pygame.key.get_pressed()

        if key_pressed[K_w] or key_pressed[K_UP]:
            me.moveup()

        if key_pressed[K_a] or key_pressed[K_LEFT]:
            me.moveleft()


        if key_pressed[K_s] or key_pressed[K_DOWN]:
            me.movedown()


        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            me.moveright()

        
            


        clock.tick(60)        
        
        

        #飞机动态频率
        if not (judge_num % 5):
            switch_plane = not switch_plane
        judge_num -= 1
        if not judge_num:
            judge_num = 100

            
        #碰撞检测
        enemy_down = pygame.sprite.spritecollide(me, all_enemys, False, pygame.sprite.collide_mask)
        if enemy_down:
            me.alive = False
            for e in enemy_down:
                e.alive = False

        

                
        #检测子弹是否击中
        for b in bullets:
            enemy_hit = pygame.sprite.spritecollide(b, all_enemys, False, pygame.sprite.collide_mask)
            if enemy_hit:
                b.alive = False
                for e in enemy_hit:
                    if e in m_enemys or e in b_enemys:
                        e.hp -= 1
                        if e.hp <= 0:
                            e.alive = False
                            if e in m_enemys:
                                all_grade += 6000
                            else:
                                all_grade += 12000
                            
                    else:
                        e.alive = False
                        all_grade += 3000
                        
                        
        #检测主角是否得到炸弹
        if bomb_rec:
            for e in bomb_rec:
                if e.alive == True:
                    e.move()
                    screen.blit(e.image_1, e.rect)
                    if pygame.sprite.collide_mask(me, e):
                        bomb_num += 1
                        e.alive = False
    
        #检测是否得到超级子弹
        if super_rec:
            for e in super_rec:
                if e.alive == True:
                    e.move()
                    screen.blit(e.image_2, e.rect)
                    if pygame.sprite.collide_mask(me, e):
                        is_super = True
                        e.alive = False
        


        #绘制飞机
        if me.alive:
            if switch_plane:
                screen.blit(me.image_2, me.rect)
            else:
                screen.blit(me.image_1, me.rect)
        else:
            screen.blit(me.d_image[my_plane_index], me.rect)
            my_plane_index = (my_plane_index + 1) % 4
            if my_plane_index == 0:
                pass


        #绘制敌人(小中大飞机)依靠存活状态检测是否毁灭
        for each in all_enemys:
            each.move()
            if each.alive:
                if each not in s_enemys:
                    pygame.draw.line(screen, BLACK, (each.rect.left, each.rect.top - 5),\
                                     (each.rect.right, each.rect.top - 5), 3)
                    hp_res = each.hp / enemy.BEnemy.hp
                    if hp_res:
                        pygame.draw.line(screen, GREEN, (each.rect.left, each.rect.top - 5), \
                                         (each.rect.left + each.rect.width * hp_res, each.rect.top - 5), 3)
                if each in b_enemys:
                    if switch_plane:
                        screen.blit(each.image_1, each.rect)
                    else:
                        screen.blit(each.image_2, each.rect)

                    
                else:
                    screen.blit(each.image, each.rect)

            else:
                if each not in b_enemys:
                    screen.blit(each.d_image[enemy_index], each.rect)
                    enemy_index = (enemy_index + 1) % 4
                    if enemy_index == 0:
                        each.kill()
                   
                else:
                    screen.blit(each.d_image[b_enemy_index], each.rect)
                    b_enemy_index = (b_enemy_index + 1) % 6
                    if b_enemy_index == 0:
                        each.kill()

        #绘制分数
        grade_text = grade_font.render("grade: %s" % str(all_grade), True, WHITE)
        screen.blit(grade_text, (10, 5))

        #绘制子弹
        for each in bullets:
            each.moveup()
            if each.alive:
                if not is_super:
                    screen.blit(each.image, each.rect)
                else:
                    screen.blit(each.image_super, each.rect)
            else:
                each.kill()
                    
        #绘制炸弹数量
        bomb_text = bomb_font.render("X %d" % bomb_num, True, WHITE)
        text_rect = bomb_text.get_rect()
        screen.blit(bomb_image, (10, bg_rect.height - 10 - text_rect.height))
        screen.blit(bomb_text, (20 + text_rect.width, bg_rect.height - 5 - text_rect.height))

        
        #刷新界面
        pygame.display.flip()


if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
    

