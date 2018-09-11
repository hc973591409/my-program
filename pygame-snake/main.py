#!C:\Program Files (x86)\Python37-32
import pygame
import sys
import time
from define import *
from game_sprites import *
import random
from pygame.locals import *


class GameStart:
    """
    游戏主体类
    """
    def __init__(self):
        """
            1、游戏py的初始化
            2、游戏屏幕设定
                显示进入游戏界面
            3、游戏时钟设定
            4、游戏精灵和精灵组的创建
        """
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE.size)
        pygame.display.set_caption("贪吃蛇")
        # 游戏时钟
        self.__clock = pygame.time.Clock()
        self.__sprite_list = []
        self.head_group = pygame.sprite.Group()
        self.score = 0
        self.__create_sprite()

    def __create_sprite(self):
        """创建蛇头身体精灵"""
        self.head_sprite = SnakeHead()
        self.body_sprite = SnakeBody()
        self.__sprite_list.append(self.head_sprite)
        self.__sprite_list.append(self.body_sprite)

        for sprite in self.__sprite_list:
            self.head_group.add(sprite)

        # 创建食物body
        self.food_sprite = SnakeFood()
        self.food_sprite.rect.x = random.randint(0, WIDTH-self.food_sprite.rect.width)
        self.food_sprite.rect.y = random.randint(0, HEIGHT-self.food_sprite.rect.height)
        self.food_group = pygame.sprite.Group(self.food_sprite)

    def travel_snake(self):
        n = len(self.__sprite_list)
        for index in range(n-1, 0, -1):
            self.__sprite_list[index].direction = self.__sprite_list[index-1].direction
            if self.__sprite_list[index].direction == 'W':
                self.__sprite_list[index].rect.x = self.__sprite_list[index-1].rect.x
                self.__sprite_list[index].rect.y = self.__sprite_list[index-1].rect.y + 25

            elif self.__sprite_list[index].direction == 'S':
                self.__sprite_list[index].rect.x = self.__sprite_list[index-1].rect.x
                self.__sprite_list[index].rect.y = self.__sprite_list[index-1].rect.y - 25

            elif self.__sprite_list[index].direction == 'A':
                self.__sprite_list[index].rect.x = self.__sprite_list[index-1].rect.x + 25
                self.__sprite_list[index].rect.y = self.__sprite_list[index-1].rect.y

            elif self.__sprite_list[index].direction == 'D':
                self.__sprite_list[index].rect.x = self.__sprite_list[index-1].rect.x - 25
                self.__sprite_list[index].rect.y = self.__sprite_list[index-1].rect.y

            self.__sprite_list[index].speed = self.__sprite_list[index-1].speed

    def update_sprites(self):
        self.head_group.update()
        self.head_group.draw(self.screen)

        self.food_group.update()
        self.food_group.draw(self.screen)

        pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("游戏退出")
                pygame.quit()
                sys.exit(0)
        # 使用键盘提供的方法 返回值为按键列表，判断按键是什么
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]:
            if self.head_sprite.direction == 'D':
                self.head_sprite.speed = MOVE_SPEED
            else:
                self.head_sprite.direction = 'D'
                self.head_sprite.speed = MOVE_SPEED

        elif key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]:
            if self.head_sprite.direction == 'A':
                self.head_sprite.speed = MOVE_SPEED
            else:
                self.head_sprite.direction = 'A'
                self.head_sprite.speed = MOVE_SPEED

        elif key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_w]:
            if self.head_sprite.direction == 'W':
                self.head_sprite.speed = MOVE_SPEED
            else:
                self.head_sprite.direction = 'W'
                self.head_sprite.speed = MOVE_SPEED

        elif key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_s]:
            if self.head_sprite.direction == 'S':
                self.head_sprite.speed = MOVE_SPEED
            else:
                self.head_sprite.direction = 'S'
                self.head_sprite.speed = MOVE_SPEED
        else:
            self.head_sprite.speed = MOVE_SPEED

    def start_game(self):
        self.enter_game()
        while True:
            self.__check_food()
            self.travel_snake()
            bg_color = (150, 0, 0)
            self.screen.fill(bg_color)
            self.__event_handler()
            self.__clock.tick(UPDATE_RATE)
            self.update_sprites()
            self.is_over()

    def enter_game(self):
        image = pygame.image.load(r"./images/main1.png").convert_alpha()
        self.screen.blit(image, (0, 0))
        pygame.display.update()
        while True:
            time.sleep(0.1)
            print("没有吗")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("游戏退出")
                    pygame.quit()
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    print("按下按键")
                    return

    def is_over(self):
        if self.head_sprite.rect.x < 0 or self.head_sprite.rect.right > WIDTH:
            self.game_over()
        elif self.head_sprite.rect.y < 0 or self.head_sprite.rect.bottom > HEIGHT:
            self.game_over()

    def __check_food(self):
        # 检测是否吃到食物, 撞到食物的时候, 尾部插入到蛇形列表
        crash = pygame.sprite.groupcollide(
            self.head_group, self.food_group, False, True)
        if len(crash) > 0:
            food_sprite = SnakeBody()
            print("吃到食物")
            self.__sprite_list.append(food_sprite)
            self.head_group.add(food_sprite)
            self.food_apear()

    def food_apear(self):
        if len(self.food_group) == 0:
            food_sprite = SnakeFood()
            food_sprite.rect.x = random.randint(0, WIDTH - self.food_sprite.rect.width)
            food_sprite.rect.y = random.randint(0, HEIGHT - self.food_sprite.rect.height)
            self.food_group.add(food_sprite)

    def game_over(self):

        self.score = (len(self.__sprite_list)) * 10
        font = pygame.font.SysFont('Mircosoft Yahei', 36)
        string = "score: %d" % self.score
        white = (255, 0, 255)
        tip = font.render(string, True, white)

        image = pygame.image.load(r"./images/gameover.png").convert_alpha()
        self.screen.blit(image, (0, 0))
        self.screen.blit(tip, (240, 150))
        pygame.display.update()
        while True:
            time.sleep(0.1)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("游戏退出")
                    pygame.quit()
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    print("按下按键")
                    pygame.quit()
                    sys.exit(0)


if __name__ == '__main__':
    game = GameStart()
    game.start_game()
    input("press any key to exit")
