# 创建一个空的Pygame窗口

import sys
import pygame

def run_game():
    # 初始化游戏并创建屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Blue Sky")

    bg_color = (240,255,255)

    #开始主循环
    while True:

        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环时都重绘屏幕
        screen.fill(bg_color)

        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()