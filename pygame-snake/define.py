import pygame

WIDTH = 720
HEIGHT = 576
SCREEN_SIZE = pygame.Rect(0, 0, WIDTH, HEIGHT)      # 游戏屏幕大小的设定
UPDATE_RATE = 4
MOVE_SPEED = 25
FOOD = pygame.USEREVENT

if __name__ == '__main__':
    print(SCREEN_SIZE.width)
