import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png") #練習3：こうかとん画像Surfaceの作成
    kk_img = pg.transform.flip(kk_img, True, False) #練習3：こうかとん画像Surfaceの反転
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = -tmr
        screen.blit(bg_img, [x, 0]) #練習5：背景画像が流れる
        screen.blit(kk_img, [300, 200]) #練習4：こうかとんSurfaceを貼り付け
        pg.display.update()
        tmr += 1        
        clock.tick(200) #FPSを200に設定することで、背景画像が早く流れるようになる


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()