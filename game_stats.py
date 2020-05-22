# 游戏统计的信息
import json


class GameStats():
    def __init__(self, set):
        self.set = set
        self.reset_stats()
        self.game_active = False
        with open("high_score.json", "r") as h_s:
            self.high_score = json.load(h_s)

        """让初始化可以在创建对象后随时发生"""
        """初始化一次放上面,重复初始化放下面  """

    def reset_stats(self):
        self.ship_life = self.set.ship_life
        self.score = 0
        self.level = 1
        """在这里初始化,在set里方便修改,开挂."""
