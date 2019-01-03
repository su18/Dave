#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.


"""
Operate
"""

import threading
from . import mouse
from . import scene

mouse_lock = threading.Lock()


def use_seed(seed, *crood):
    mouse_lock.acquire()
    mouse.safe_click()
    scene.click_seed(seed)
    scene.click_grid(*crood)
    mouse.safe_click()
    mouse_lock.release()


def use_shovel(*crood):
    mouse_lock.acquire()
    mouse.safe_click()
    scene.click_shovel()
    scene.click_grid(*crood)
    mouse.safe_click()
    mouse_lock.release()
