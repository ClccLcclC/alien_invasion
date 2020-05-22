import pygame.sysfont

"""能够将文本渲染到屏幕上"""


class Button():
    def __init__(self, screen, msg):
        self.screen = screen
        width, height = 200, 50
        screen_rect = screen.get_rect()
        self.button_rect = pygame.Rect(0, 0, width, height)
        self.button_rect.center = screen_rect.center
        self.text_color = (255, 255, 255)
        self.button_color = (0, 255, 0)
        self.font = pygame.font.SysFont(None, 48)  # 使用默认字体,48字号大小
        self.create_label(msg)
        """放到函数并初始化是为了开始创建一次,以后调用的时候再创建"""
        """把一段开头要用的和后面运行的要用的放到一个函数内,并初始化"""

    def create_label(self, msg):
        """一个由文字对象渲染成外接矩形图像,用函数font"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.button_rect.center
        # msg_image 就是一个由文本渲染成的图像

    def draw_button(self):
        self.screen.fill(self.button_color, self.button_rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        # 创建图像的先后顺序决定了图像的层面