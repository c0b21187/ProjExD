import pygame as pg # pygameをimport
import sys          # systemをimport
import random       # randomをimport

def main():
    clock = pg.time.Clock()

    # 練習1
    pg.display.set_caption("逃げろ！こうかとん")   # 逃げろこうかとんを題名に表示させる
    screen_sfc = pg.display.set_mode((1300, 700)) # Surface
    screen_rct = screen_sfc.get_rect()            # Rect
    bgimg_sfc = pg.image.load("fig/halloweenyoru491.png") # 背景画像を入れる
    bgimg_rct = bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc, bgimg_rct)


    kkimg_sfc = pg.image.load("fig/6.png") # こうかとんの画像を選ぶ
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)
    kkimg_rct = kkimg_sfc.get_rect()
    kkimg_rct.center = 900, 500 # こうかとんの出現位置

    bmimg_sfc1 = pg.image.load("fig/ghost_halloween.png") # 1体目のお化け
    bmimg_sfc1 = pg.transform.rotozoom(bmimg_sfc1,0, 0.09)
    bmimg_rct1 = bmimg_sfc1.get_rect()
    bmimg_rct1.centerx = random.randint(0, screen_rct.width)
    bmimg_rct1.centery = random.randint(0, screen_rct.height)

    bmimg_sfc2 = pg.image.load("fig/ghost_halloween.png") # 2体目のお化け
    bmimg_sfc2 = pg.transform.rotozoom(bmimg_sfc2,0, 0.09)
    bmimg_rct2 = bmimg_sfc2.get_rect()
    bmimg_rct2.centerx = random.randint(0, screen_rct.width)
    bmimg_rct2.centery = random.randint(0, screen_rct.height)

    bmimg_sfc3 = pg.image.load("fig/ghost_halloween.png") # 3体目のお化け
    bmimg_sfc3 = pg.transform.rotozoom(bmimg_sfc3,0, 0.09)
    bmimg_rct3 = bmimg_sfc3.get_rect()
    bmimg_rct3.centerx = random.randint(0, screen_rct.width)
    bmimg_rct3.centery = random.randint(0, screen_rct.height)

    vx1, vy1 = +1 ,+1
    vx2, vy2 = +1 ,+1
    vx3, vy3 = +1 ,+1
    

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)

        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]    == True:kkimg_rct.centery -= 1 # 上に動かす
        if key_states[pg.K_DOWN]  == True:kkimg_rct.centery += 1 # 下に動かす
        if key_states[pg.K_LEFT]  == True:kkimg_rct.centerx -= 1 # 左に動かす
        if key_states[pg.K_RIGHT] == True:kkimg_rct.centerx += 1 # 右に動かす

        if check_bound(kkimg_rct, screen_rct) != (1, 1):
            if key_states[pg.K_UP]    == True:kkimg_rct.centery += 1
            if key_states[pg.K_DOWN]  == True:kkimg_rct.centery -= 1
            if key_states[pg.K_LEFT]  == True:kkimg_rct.centerx += 1
            if key_states[pg.K_RIGHT] == True:kkimg_rct.centerx -= 1
        screen_sfc.blit(kkimg_sfc, kkimg_rct)

        bmimg_rct1.move_ip(vx1, vy1)
        bmimg_rct2.move_ip(vx2, vy2)
        bmimg_rct3.move_ip(vx3, vy3)

        screen_sfc.blit(bmimg_sfc1, bmimg_rct1)
        screen_sfc.blit(bmimg_sfc2, bmimg_rct2)
        screen_sfc.blit(bmimg_sfc3, bmimg_rct3)

        yoko, tate = check_bound(bmimg_rct1, screen_rct)
        vx1 *= yoko
        vy1 *= tate

        yoko, tate = check_bound(bmimg_rct2, screen_rct)
        vx2 *= yoko
        vy2 *= tate

        yoko, tate = check_bound(bmimg_rct3, screen_rct)
        vx3 *= yoko
        vy3 *= tate

        if kkimg_rct.colliderect(bmimg_rct1):
            return
        if kkimg_rct.colliderect(bmimg_rct2):
            return
        if kkimg_rct.colliderect(bmimg_rct3):
            return

        pg.display.update()
        clock.tick(1000)

def check_bound(rct, scr_rct):

    yoko, tate = +1, +1
    if rct.left < scr_rct.left or scr_rct.right < rct.right :yoko = -1 # 領域外
    if rct.top < scr_rct.top or scr_rct.bottom < rct.bottom :tate = -1 # 領域外
    return yoko, tate


if __name__ == "__main__":
    pg.init()      # モジュールを初期化する
    main()         # これから実装するゲームのメイン部分
    pg.quit()      # モジュールの初期化の解除する
    sys.exit()     # プログラムを終了する