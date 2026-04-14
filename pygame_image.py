import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #練習１:背景画像
    tmr = 0
    koukaton = pg.image.load("fig/3.png") #練習3:コウカトン読み込み
    koukaton = pg.transform.flip(koukaton, True ,False)#練習3:コウカトンの反転(関数,左右,上下)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        screen.blit(bg_img, [0, 0]) #練習2
        screen.blit(koukaton,[300,200]) #練習４：コウカトンの初期位置
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()