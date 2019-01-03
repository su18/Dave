#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.

from plugins import *


class ZenGarden(object):

    def __init__(self, chocolate, pesticide, flower_fertilizers, tree_fertilizers):
        self.chocolate = chocolate + 1000
        self.pesticide = pesticide + 1000
        self.flower_fertilizers = flower_fertilizers + 1000
        self.tree_fertilizers = tree_fertilizers + 1000

    def write_chocolate(self):
        WriteMemory('int', self.chocolate, 0x6a9ec0, 0x82c, 0x228)

    def write_pesticide(self):
        WriteMemory('int', self.pesticide, 0x6a9ec0, 0x82c, 0x1FC)

    def write_flower_fertilizers(self):
        WriteMemory('int', self.flower_fertilizers, 0x6a9ec0, 0x82c, 0x1F8)

    def write_tree_fertilizers(self):
        WriteMemory('int', self.tree_fertilizers, 0x6a9ec0, 0x82c, 0x230)

    @staticmethod
    def rich_second_generation():
        WriteMemory('bool', 0, 0x6a9ec0, 0x82c, 0x204)
