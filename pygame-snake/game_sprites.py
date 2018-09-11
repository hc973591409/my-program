import pygame
from define import *


class SnakeSprite(pygame.sprite.Sprite):
    """蛇由一个个方块加上头节点组成"""
    def __init__(self, image_name, speed=MOVE_SPEED, pre=None):
        super().__init__()
        # 当前方块的位置
        # 当前方块的方向，W(up), S(down) A(left) D(right)
        self.direction = 'D'
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        print(self.rect)
        # 默认速度为 1，当向相同方向移动的时候就加速
        self.speed = speed
        self.pre = pre

    def pre_direction(self):
        self.direction = self.pre.direction

    def update(self):
        # 获取下一个节点的方向
        self.pre_direction()


class SnakeHead(SnakeSprite):
    def __init__(self):
        """
        蛇头
        """
        super().__init__("./images/head.png")
        self.rect.x = 100
        self.rect.y = 100

    def update(self):
        if self.direction == 'D':
            self.rect.x += self.speed

        elif self.direction == 'A':
            self.rect.x -= self.speed

        elif self.direction == 'W':
            self.rect.y -= self.speed

        elif self.direction == 'S':
            self.rect.y += self.speed


class SnakeBody(SnakeSprite):
    """蛇身体类"""
    def __init__(self):
        super().__init__("./images/body.png")
        self.rect.x = 75
        self.rect.y = 100

    def update(self):
        if self.direction == 'D':
            self.rect.x += self.speed

        elif self.direction == 'A':
            self.rect.x -= self.speed

        elif self.direction == 'W':
            self.rect.y -= self.speed

        elif self.direction == 'S':
            self.rect.y += self.speed


class SnakeFood(SnakeSprite):
    """蛇身体类"""
    def __init__(self):
        super().__init__("./images/body.png")
        self.rect.x = 200
        self.rect.y = 400

    def update(self):
        pass
