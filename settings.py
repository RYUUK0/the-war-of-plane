import os


NOW_PATH = os.path.abspath(__file__)
BASE_PATH = os.path.dirname(NOW_PATH)
#print(BASE_PATH)

#图片声音字体地址
IMG_PATH = BASE_PATH + '\\images'
SOUND_PATH = BASE_PATH + '\\sound'
FONT_PATH = BASE_PATH + '\\font'



#背景图片
background = IMG_PATH + '\\background1.png'

#子弹图片
normal_bullet = IMG_PATH + '\\bullet1.png'
super_bullet = IMG_PATH + '\\bullet2.png'

#敌方飞机图片（小中大）
small_enemy = IMG_PATH + '\\enemy1.png'
normal_enemy = IMG_PATH + '\\enemy2.png'
big_enemy_one = IMG_PATH + '\\enemy3_n1.png'
big_enemy_two = IMG_PATH + '\\enemy3_n2.png'

#地方飞机毁灭画面

#小
small_enemy_destroy_1 = IMG_PATH + '\\enemy1_down1.png'
small_enemy_destroy_2 = IMG_PATH + '\\enemy1_down2.png'
small_enemy_destroy_3 = IMG_PATH + '\\enemy1_down3.png'
small_enemy_destroy_4 = IMG_PATH + '\\enemy1_down4.png'

#中
normal_enemy_destroy_1 = IMG_PATH + '\\enemy2_down1.png'
normal_enemy_destroy_2 = IMG_PATH + '\\enemy2_down2.png'
normal_enemy_destroy_3 = IMG_PATH + '\\enemy2_down3.png'
normal_enemy_destroy_4 = IMG_PATH + '\\enemy2_down4.png'

#大
big_enemy_destroy_1 = IMG_PATH + '\\enemy3_down1.png'
big_enemy_destroy_2 = IMG_PATH + '\\enemy3_down2.png'
big_enemy_destroy_3 = IMG_PATH + '\\enemy3_down3.png'
big_enemy_destroy_4 = IMG_PATH + '\\enemy3_down4.png'
big_enemy_destroy_5 = IMG_PATH + '\\enemy3_down5.png'
big_enemy_destroy_6 = IMG_PATH + '\\enemy3_down6.png'



#主角飞机图片
me_1 = IMG_PATH + '\\me3.png'
me_2 = IMG_PATH + '\\me4.png'

#主角飞机损坏
me_destroy_1 = IMG_PATH + '\\me_destroy_1.png'
me_destroy_2 = IMG_PATH + '\\me_destroy_2.png'
me_destroy_3 = IMG_PATH + '\\me_destroy_3.png'
me_destroy_4 = IMG_PATH + '\\me_destroy_4.png'

#道具图片
bomb = IMG_PATH + '\\bomb.png'
#特殊道具补给图片
bomb_supply = IMG_PATH + '\\bomb_supply.png'
bullet_supply = IMG_PATH + '\\bullet_supply.png'

#字体文件
grade_font = 'font\\font.ttf'


