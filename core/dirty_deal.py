#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.

from plugins import *


class DirtyDeal(object):

    def __init__(self, sunshine, gold):
        self.sunshine = sunshine
        self.gold = int(gold / 10)

    def write_sunshine(self):
        WriteMemory("int", self.sunshine, 0x6a9ec0, 0x768, 0x5560)

    def write_gold(self):
        WriteMemory("int", self.gold, 0x6a9ec0, 0x82c, 0x28)
