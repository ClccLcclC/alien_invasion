import pygame.sysfont
import pygame.sprite
import ship


# 将文本渲染为图像
class Scoreboard():
    def __init__(self, stats, set, screen):
        self.stats = stats
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.set = set
        self.score_text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)  # 可以理解为文本设置
        self.draw_score()
        self.draw_hight_score()
        self.draw_level()
        self.show_ships()
        # pygame里的函数

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.hight_score_image, self.hight_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.level_sign_image, self.level_sign_rect)
        self.ships.draw(self.screen)

    def draw_score(self):
        # 文本须为字符串,round让小数精确到小数点后几位,负数时则精确到10,100,1000最近的位数
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        # 一种格式代码,记住便是
        self.score_image = self.font.render(score_str, True, self.score_text_color, self.set.background_color)
        """放在屏幕的右上角"""
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def draw_hight_score(self):
        rounded_hight_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(rounded_hight_score)
        # 一种格式代码,记住便是
        self.hight_score_image = self.font.render(high_score_str, True, self.score_text_color,
                                                  self.set.background_color)
        """放在屏幕的正上角"""
        self.hight_score_rect = self.hight_score_image.get_rect()
        self.hight_score_rect.centerx = self.screen_rect.centerx
        self.score_rect.top = self.screen_rect.top

    def draw_level(self):
        self.level_image = self.font.render(str(self.stats.level), True, self.score_text_color,
                                            self.set.background_color)
        """放在得分的下方"""
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        self.level_sign_image = self.font.render("Level", True, self.score_text_color,
                                                 self.set.background_color)
        self.level_sign_rect = self.level_sign_image.get_rect()
        self.level_sign_rect.right = self.score_rect.right - self.level_rect.width - 5
        # 当发现运行正常图像没出现时,多考虑xy轴问题
        self.level_sign_rect.top = self.score_rect.bottom + 10

    def show_ships(self):
        self.ships = pygame.sprite.Group()
        for ship_number in range(self.stats.ship_life):
            ship_0 = ship.Ship(self.screen, self.set)
            # 注意参数位置,切记切记
            ship_0.ship_rect.left = 10 + int(ship_number) * ship_0.ship_rect.width
            ship_0.ship_rect.top = 10
            self.ships.add(ship_0)
