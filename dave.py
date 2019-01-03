#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.


import time
from core.dirty_deal import DirtyDeal
from core.bombing_area import BombingArea
from core.no_cooldown import no_cool_down
from core.gatling_gun import gatling_gun
from core.auto_collect import auto_collect
from core.zen_garden import ZenGarden
from core.puzzle_solve import PuzzleSolve


time.sleep(3)

# 更改阳光和金钱值
# increase = DirtyDeal(sunshine=4586, gold=56790)
# increase.write_sunshine()
# increase.write_gold()

# 自动收集场上阳光和钻石
# auto_collect()

# 植物种植无冷却
# while True:
#     no_cool_down()

# 加特林模式
# gatling_gun()


# 轰炸区
bombing = BombingArea(zone='all', times=20, time_interval=0.5, plant_type='Cherry Bomb')
bombing.dropping_bomb()


# 禅境花园巧克力、杀虫剂、花肥、树肥自定义
# zen = ZenGarden(chocolate=56, pesticide=25, flower_fertilizers=22, tree_fertilizers=12)
# zen.write_chocolate()
# zen.write_flower_fertilizers()
# zen.write_pesticide()
# zen.write_tree_fertilizers()


# 解谜模式
# puzzle = PuzzleSolve(vase_see_through=True,)
# puzzle.vase_breaker()


# whosyourdaddy
