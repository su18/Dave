#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.


import gc
import atexit
from . import mouse, utils, win32, process, scene, seeds
from .process import find_pvz_1051 as FindPvZ
from .process import read_memory as ReadMemory
from .process import write_memory as WriteMemory
from .mouse import left_click as LeftClick
from .mouse import right_click as RightClick
from .mouse import safe_click as SafeClick
from .mouse import special_button_click as ButtonClick
from .delay import thread_sleep_for as Sleep
from .delay import game_delay_for as Delay
from .delay import until_countdown as Countdown
from .delay import until_relative_time_after_refresh as Prejudge
from .delay import until_relative_time as Until
from .scene import click_seed as ClickSeed
from .scene import click_shovel as ClickShovel
from .scene import click_grid as ClickGrid
from .operate import use_seed as Card
from .operate import use_shovel as Shovel
from .threads import running_in_thread as RunningInThread
from .threads import auto_collect as StartAutoCollectThread
from .threads import immobilize_dancer as StartStopDancerThread

__all__ = [
    "FindPvZ",
    "ReadMemory",
    "WriteMemory",
    "LeftClick",
    "RightClick",
    "SafeClick",
    "ButtonClick",
    "Sleep",
    "Delay",
    "Countdown",
    "Prejudge",
    "Until",
    "ClickSeed",
    "ClickShovel",
    "ClickGrid",
    "Card",
    "Shovel",
    "RunningInThread",
    "StartAutoCollectThread",
    "StartStopDancerThread",
]
pvz_priority_class_original = win32.NORMAL_PRIORITY_CLASS


def on_start():
    win32.timeBeginPeriod(1)
    gc.disable()
    win32.SetPriorityClass(win32.GetCurrentProcess(), win32.HIGH_PRIORITY_CLASS)
    mouse.get_dpi_scale()
    if process.find_pvz_1051():
        global pvz_priority_class_original
        pvz_priority_class_original = win32.GetPriorityClass(process.pvz_handle)
        if pvz_priority_class_original != win32.REALTIME_PRIORITY_CLASS:
            win32.SetPriorityClass(process.pvz_handle, win32.HIGH_PRIORITY_CLASS)

        if utils.game_ui() in (2, 3):
            global slots_count, game_scene
            slots_count = process.read_memory("int", 0x6A9EC0, 0x768, 0x144, 0x24)
            game_scene = process.read_memory("int", 0x6A9EC0, 0x768, 0x554C)
            seeds.update_seeds_list()  # utils.game_ui() in (3,)
            scene.update_game_scene()


def on_exit():
    win32.timeEndPeriod(1)
    if process.is_valid():
        win32.SetPriorityClass(process.pvz_handle, pvz_priority_class_original)
        win32.CloseHandle(process.pvz_handle)
on_start()
atexit.register(on_exit)
