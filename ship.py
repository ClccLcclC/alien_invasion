import pygame
import pygame.sprite

class Ship(pygame.sprite.Sprite):
    def __init__(self, screen, set):  # 需要屏幕对象来创建飞船
        super().__init__()
        self.screen = screen
        self.set = set
        self.image=pygame.image.load("ship.bmp")  # 创建好了ship
        self.ship_image = self.image
        self.rect = self.ship_image.get_rect()
        self.ship_rect = self.rect
        self.screen_rect = self.screen.get_rect()  # 获取ship和屏幕的外接矩形
        self.ship_rect.centerx = self.screen_rect.centerx  #
        self.ship_rect.bottom = self.screen_rect.bottom  # ship底部坐标和屏幕Y相同
        self.ship_speed_factor = 1.5
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False  # 设置标志,监听事件只改变标志
        self.moving_down = False
         # 为了精确控制，采用浮点型
        self.ship_rect.centerx = float(self.ship_rect.centerx)
        self.ship_rect.centery = float(self.ship_rect.centery)

    def update(self):  # 必须都用if不然当同时按住时会往左边跑
        if self.moving_left and (self.ship_rect.left > self.screen_rect.left):
            self.ship_rect.centerx -= self.set.ship_speed_factor
        if self.moving_right and (self.ship_rect.right < self.screen_rect.right):
            self.ship_rect.centerx += self.set.ship_speed_factor
        if self.moving_up and (self.ship_rect.top > self.screen_rect.top):
            self.ship_rect.centery -= self.set.ship_speed_factor
        if self.moving_down and (self.ship_rect.bottom < self.screen_rect.bottom):
            self.ship_rect.centery += self.set.ship_speed_factor

    def create_ship(self):
        self.screen.blit(self.ship_image , self.ship_rect)  # 创建ship,此时还未显示

    def center_ship(self):
        self.ship_rect.centerx = self.screen_rect.centerx
        self.ship_rect.bottom = self.screen_rect.bottom