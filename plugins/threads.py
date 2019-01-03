#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.

import functools
import threading
import time
from plugins import process, keyboard, operate
from . import utils
from . import mouse


def running_in_thread(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()

    return wrapper


@running_in_thread
def auto_collect(collect_items=[1, 2, 3, 4, 5, 6, 17], interval_cs=12):
    interval = interval_cs / 100
    while utils.game_ui() != 3:
        time.sleep(0.1)
    while utils.game_ui() == 3:
        item_count = process.read_memory("int", 0x6A9EC0, 0x768, 0xF4)
        item_count_max = process.read_memory("int", 0x6A9EC0, 0x768, 0xE8)
        item_offset = process.read_memory("int", 0x6A9EC0, 0x768, 0xE4)

        if item_count == 0:
            time.sleep(interval)
            continue

        uncollected_item_count = 0
        for i in range(item_count_max):
            disappeared = process.read_memory("bool", item_offset + 0x38 + 0xD8 * i)
            collected = process.read_memory("bool", item_offset + 0x50 + 0xD8 * i)
            item_type = process.read_memory("int", item_offset + 0x58 + 0xD8 * i)
            if not disappeared and not collected and item_type in collect_items:
                uncollected_item_count += 1
        if uncollected_item_count == 0:
            time.sleep(interval * 3)
            continue

        for i in range(item_count_max):
            if utils.game_ui() != 3:
                break
            while utils.game_paused() or utils.mouse_in_game():
                time.sleep(interval)

            disappeared = process.read_memory("bool", item_offset + 0x38 + 0xD8 * i)
            collected = process.read_memory("bool", item_offset + 0x50 + 0xD8 * i)
            item_type = process.read_memory("int", item_offset + 0x58 + 0xD8 * i)
            if not disappeared and not collected and item_type in collect_items:

                item_x = process.read_memory("float", item_offset + 0x24 + 0xD8 * i)
                item_y = process.read_memory("float", item_offset + 0x28 + 0xD8 * i)
                if item_x >= 0.0 and item_y >= 70.0:
                    operate.mouse_lock.acquire()
                    mouse.safe_click()
                    x, y = int(item_x + 30), int(item_y + 30)
                    mouse.left_click(x, y)
                    mouse.safe_click()
                    operate.mouse_lock.release()
                    time.sleep(interval)


ice_spots = []


@running_in_thread
def immobilize_dancer():
    while utils.game_ui() != 3:
        time.sleep(0.01)
    while utils.game_ui() == 3:
        while (((utils.dance_clock() + 10) % (23 * 20)) // 20) > 11:
            time.sleep(0.01)
        keyboard.pause_game()
        time.sleep(0.5)
        while (((utils.dance_clock()) % (23 * 20)) // 20) <= 11:
            time.sleep(0.01)
        keyboard.restore_game()
