import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False) #練習8：左右反転した背景画像Surface
    kk_img = pg.image.load("fig/3.png") #練習3：こうかとん画像Surfaceの作成
    kk_img = pg.transform.flip(kk_img, True, False) #練習3：こうかとん左右反転
    kk_rct = kk_img.get_rect() #練習10-1
    kk_rct.center = 300, 200 #練習10-2
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed() #練習10-3
        # print(key_lst[pg.K_UP], key_lst[pg.K_DOWN], key_lst[pg.K_LEFT], key_lst[pg.K_RIGHT]) 

        move_default_x_speed = -1
        move_default_y_speed = 0
        add_x_speed = 0
        add_y_speed = 0
        

        if key_lst[pg.K_UP]:
            add_y_speed = -1
        if key_lst[pg.K_DOWN]:
            add_y_speed = +1
        if key_lst[pg.K_RIGHT]:
            add_x_speed = +2
        if key_lst[pg.K_LEFT]:
            add_x_speed = -1
        
        x_speed = move_default_x_speed + add_x_speed
        y_speed = move_default_y_speed + add_y_speed
        
        kk_rct.move_ip(x_speed, y_speed)

        x = tmr%3200 # 練習9：ループさせる
        screen.blit(bg_img, [-x, 0]) #練習5：背景画像を右から左に
        screen.blit(bg_img2, [-x+1600, 0]) #練習7：2枚目の背景画像
        screen.blit(bg_img, [-x+3200, 0]) #練習9：3枚目の背景画像
        screen.blit(kk_img, kk_rct) #練習4：こうかとんSurfaceを貼り付け
        pg.display.update()
        tmr += 1        
        clock.tick(200)  # 練習6：FPS変更


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()