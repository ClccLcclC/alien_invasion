import pygame
import pygame.sprite


class Alien(pygame.sprite.Sprite):
    def __init__(self, screen, set):
        super().__init__()
        self.screen = screen
        self.set = set
        self.image = pygame.image.load("alien.bmp")
        self.alien_image=self.image
        self.rect = self.alien_image.get_rect()
        self.alien_rect = self.rect
        """加载外星人图片,并且获得rect"""
        self.alien_rect.left = self.alien_rect.width
        self.alien_rect.top = self.alien_rect.height
        """外星人的左边距为外星人的宽度,上边距为外星人的高度"""
        self.alien_rect.left = float(self.alien_rect.left)

    def create_alien(self):
        self.screen.blit(self.alien_image, self.alien_rect)  # 将创建alien此时还未显示

    # 改变外星人的位置
    def update(self):
        self.alien_rect.left += (self.set.alien_speed_factor * self.set.fleet_direction)

    # 检测外星是否碰撞墙壁
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.alien_rect.right >= screen_rect.right:
            return True
        if self.alien_rect.left <= 0:
            return True
