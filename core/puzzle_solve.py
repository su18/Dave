#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.

from plugins import *


class PuzzleSolve(object):

    def __init__(self, vase_see_through):
        self.vase_see_through = vase_see_through

    @RunningInThread
    def vase_breaker(self):
        for i in range(36):
            a = 0x4c + 0xec*i
            WriteMemory("int", 30000000, 0x6a9ec0, 0x768, 0x11c, a)

