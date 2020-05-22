import pygame
import sys
import bullet
import alien
import time
import json
from pygame import sprite


# 监听事件
def check_events(ship, screen, bullets, set, play_button, stats):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open("high_score.json", "w") as h_s:
                json.dump(stats.high_score, h_s)      
            sys.exit()                               
        if event.type == pygame.KEYDOWN:  # 检测到按键按下
            check_keydown_events(event, ship, screen, bullets, set, stats)
        if event.type == pygame.KEYUP:  # 检测到按键松开
            check_keyup_events(event, ship)
        """还没检测到按键松开就关闭了检测按键松开"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # 返回一个元组,元组x,y为鼠标点击的坐标
            check_play_button(mouse_x, mouse_y, play_button, stats)


# 重绘屏幕
def update_screen(set, screen, ship_1, bullets, aliens, stats, play_button, sb):
    screen.fill(set.background_color)  # 更换屏幕颜色
    ship_1.create_ship()  # 不断的在新subface创建飞船
    # for alien in aliens.sprites():
    #     alien.create_alien()
    aliens.draw(screen)  # 因为对sprite函数的不了解,他默认调用的是类中的某个名字值,无他
    sb.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    check_aliens_bottom(screen, aliens, stats, bullets, ship_1, set, sb)
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()  # 刷新


# 检测按键按下
def check_keydown_events(event, ship, screen, bullets, set, stats):
    if event.key == pygame.K_LEFT:  # 只检测按一次键
        ship.moving_left = True
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_SPACE:
        pygame.mouse.set_visible(False)
        stats.game_active = True
        create_bullet(bullets, set, screen, ship)
    if event.key == pygame.K_q:
        with open("high_score.json", "w") as h_s:
            json.dump(stats.high_score, h_s)
        sys.exit()


# 检测按键松开
def check_keyup_events(event, ship):
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False


# 更新子弹,并且删除子弹设置
def update_bullets(bullets, aliens, set, screen, ship_1, stats, sb):
    bullets.update()  # 更新bullets的位置
    # 用这个sprite创建出来的精灵组是bullet的对象集合,作为集合也可以访问对象中的属性
    # 编组会对其中的每个精灵调用update
    # 删除子弹
    for bullet in bullets.copy():
        if bullet.bullet_rect.top <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(bullets, aliens, set, ship_1, screen, stats, sb)


# 限制子弹数量,创建bullet实例
def create_bullet(bullets, set, screen, ship):
    if len(bullets) < set.bullets_allowed:
        """限制子弹数量"""
        new_bullet = bullet.Bullet(set, screen, ship)
        bullets.add(new_bullet)  # 每次按空格创建一个子弹把创建好的子弹放进这个编组里


# # 创建外星人群组
def create_fleet(screen, set, aliens, ship_1):
    alien_0 = alien.Alien(screen, set)
    alien_0_width = alien_0.alien_rect.width  # 获取外星人的宽度
    alien_0_height = alien_0.alien_rect.height  # 获取外星人的高度
    aliens_numbers_x = get_number_alien(set, alien_0_width)
    aliens_numbers_y = get_number_rows(set, alien_0_height, ship_1)
    for number in range(aliens_numbers_x):
        for rows in range(aliens_numbers_y):
            create_alien(screen, number, aliens, rows, set)


# 创建单个外星人
def create_alien(screen, number, aliens, rows, set):
    alien_0 = alien.Alien(screen, set)
    alien_0.alien_rect.left = alien_0.alien_rect.width + 2 * alien_0.alien_rect.width * number
    alien_0.alien_rect.top = alien_0.alien_rect.height + 2 * alien_0.alien_rect.height * rows
    aliens.add(alien_0)


# 计算screen可以容纳多少行机器人
def get_number_rows(set, alien_0_height, ship_1):
    """加了括号才可以分行"""
    aliens_space_y = (set.screen_height -
                      3 * alien_0_height - ship_1.ship_rect.height)
    aliens_numbers_y = int(aliens_space_y / (2 * alien_0_height))

    return aliens_numbers_y


# 获得外星人每行的数量
def get_number_alien(set, alien_0_width):
    aliens_space_x = set.screen_width - (2 * alien_0_width)
    aliens_numbers_x = int(aliens_space_x / (2 * alien_0_width))
    return aliens_numbers_x


# 把所有的外星人读一遍检测是否有碰撞
def change_fleet_edges(aliens, set):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(aliens, set)
            break


# 把所有的外星人遍历一遍,增加Y值并且,改变x轴运动放心
def change_fleet_direction(aliens, set):
    for alien in aliens.sprites():
        alien.alien_rect.top += set.fleet_drop_speed
    set.fleet_direction *= -1


def update_aliens(aliens, set, ship_1, stats, bullets, screen, sb):
    change_fleet_edges(aliens, set)
    aliens.update()
    """aliens作为精灵组也可以访问精灵对象内的函数"""
    if pygame.sprite.spritecollideany(ship_1, aliens):
        ship_hit(stats, aliens, bullets, screen, ship_1, set, sb)


"""遍历aliens检测与ship_1rect有无重叠,有的话停止遍历,返回碰撞的alien"""


def check_bullet_alien_collisions(bullets, aliens, set, ship_1, screen, stats, sb):
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
    """遍历bullets和aliens所有的rect,一旦有重叠,就在他返回的字典里添加键值对bullets-aliens"""
    if collisions:  # 返回的collisions是字典
        for aliens in collisions.values():
            stats.score += set.alien_points * len(aliens)
            if stats.score >= stats.high_score:
                stats.high_score = stats.score
            # aliens是一个列表,应对一个子弹对应多个外星人的情况,
            sb.draw_score()
            sb.draw_hight_score()
        # 重新渲染分数的图像
    if len(aliens) == 0:
        bullets.empty()
        """不是必须,但是跟程序运行流畅有关"""
        create_fleet(screen, set, aliens, ship_1)
        set.increase_speed()
        stats.level += 1
        sb.draw_level()


# 检测飞船碰撞
def ship_hit(stats, aliens, bullets, screen, ship_1, set, sb):
    if stats.ship_life > 1:
        stats.ship_life -= 1
        aliens.empty()
        bullets.empty()
        create_fleet(screen, set, aliens, ship_1)
        ship_1.center_ship()  # 子弹和外星人被清除,飞船没有,重置飞船位置
        sb.show_ships()
        time.sleep(0.5)
    else:
        stats.game_active = False
        stats.reset_stats()  # 重置等级,重置得分
        aliens.empty()
        bullets.empty()
        set.init_speed()
        create_fleet(screen, set, aliens, ship_1)
        ship_1.center_ship()
        sb.show_ships()
        pygame.mouse.set_visible(True)


def check_aliens_bottom(screen, aliens, stats, bullets, ship_1, set, sb):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(stats, aliens, bullets, screen, ship_1, set, sb)
            break


# 单机play激活游戏
def check_play_button(mouse_x, mouse_y, play_button, stats):
    if play_button.button_rect.collidepoint(mouse_x, mouse_y):
        pygame.mouse.set_visible(False)
        stats.game_active = True
