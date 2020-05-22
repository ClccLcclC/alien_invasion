import pygame
import settings
import ship
import game_functions
import pygame.sprite
import game_stats
import button
import scoreboard


def run_game():
    pygame.init()  # 初始化
    set = settings.Settings()  # 创建对象set获取Settings中的info
    screen = pygame.display.set_mode(
        (set.screen_width, set.screen_height))  # 这里填的是元组
    pygame.display.set_caption("Chenlicheng")  # 设置标题
    ship_1 = ship.Ship(screen, set)  # 创建了一艘船的实例
    bullets = pygame.sprite.Group()  # 创建了一个精灵的编组
    aliens = pygame.sprite.Group()  # 创建了一个外星人的编组
    stats = game_stats.GameStats(set)
    sb = scoreboard.Scoreboard(stats, set, screen)#创建一个积分的实例
    play_button = button.Button(screen, "play")
    game_functions.create_fleet(screen, set, aliens, ship_1)  # 创建了一些外星人,并且把它放到编组里
    while True:
        # 检查必须保持活跃,不然无法回到游戏中
        game_functions.check_events(ship_1, screen, bullets, set, play_button, stats)  # 位置实参
        if stats.game_active:  # 飞船,子弹,外星人不再刷新,但是保持屏幕active
            ship_1.update()  # 更新ship的位置
            game_functions.update_bullets(bullets, aliens, set, screen, ship_1,stats,sb)
            game_functions.update_aliens(aliens, set, ship_1, stats, bullets, screen,sb)
        game_functions.update_screen(set, screen, ship_1, bullets, aliens, stats, play_button,sb)
        # 在新屏幕重绘飞船在新屏幕重绘子弹,一个子弹射出去到消失是画了很多次的结果


run_game()
