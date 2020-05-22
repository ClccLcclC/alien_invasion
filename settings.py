class Settings():
    def __init__(self):
        self.background_color = (230, 230, 230)
        self.screen_width = 1200
        self.screen_height = 600
        self.bullet_width = 20
        self.bullet_height = 50
        self.bullet_color = (60, 60, 60) 
        self.bullets_allowed = 100
        self.fleet_direction = 1  # update函数为+=,当fleet_direction为1即为右移反之为左移
        self.ship_life = 3
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.init_speed()

    def init_speed(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 5
        self.fleet_drop_speed = 10
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.fleet_drop_speed *= self.speedup_scale
        self.alien_points *= self.score_scale
