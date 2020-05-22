import pygame
import pygame.sprite


class Bullet(pygame.sprite.Sprite):
    def __init__(self, set, screen, ship):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, set.bullet_width, set.bullet_height)
        self.bullet_rect = self.rect
        """创建一个子弹，并获得他的外接矩形"""
        self.bullet_rect.centerx = ship.ship_rect.centerx
        self.bullet_rect.bottom = ship.ship_rect.top  # 子弹从飞船外出来
        self.bullet_color = set.bullet_color
        self.bullet_speed_factor = set.bullet_speed_factor
        self.bullet_rect.top = float(self.bullet_rect.top)
        self.sign = False
    def draw_bullet(self):
        """创建了还要将他画出来才能显示在surface"""
        pygame.draw.rect(self.screen, self.bullet_color, self.bullet_rect)

    def update(self):
        """子弹创建后自动向上移动"""
        self.bullet_rect.top -= self.bullet_speed_factor

