#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.

from plugins import *


@RunningInThread
def no_cool_down():
    for i in range(0, 10):
        a = 0x50 * i + 0x70
        WriteMemory("int", 1, 0x6a9ec0, 0x768, 0x144, a)
