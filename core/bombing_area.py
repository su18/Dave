#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.

import random
import time
from plugins import *
from core.no_cooldown import no_cool_down


class BombingArea(object):

    def __init__(self, time_interval, zone, times, plant_type='Cherry Bomb'):
        self.plant_type = plant_type
        self.time_interval = time_interval
        self.zone = zone
        self.times = times
        self.row = [1, 2, 3, 4, 5]
        self.column = []

    def target_zone(self):
        if self.zone == 'left':
            self.column = [1, 2, 3, 4, 5]
        elif self.zone == 'right':
            self.column = [9, 8, 7, 6, 5]
        elif self.zone == 'all':
            self.column = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        else:
            print('wrong')
        c = random.choice(self.column)
        r = random.choice(self.row)
        return r, c

    def dropping_bomb(self):
        for t in range(self.times):
            no_cool_down()
            ClickSeed(self.plant_type)
            ClickGrid(self.target_zone())
            time.sleep(self.time_interval)
