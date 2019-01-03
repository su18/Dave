#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.

from . import process
from . import mouse, seeds

slots_count = 10
game_scene = 2


def update_game_scene():
    global slots_count, game_scene
    slots_count = process.read_memory("int", 0x6A9EC0, 0x768, 0x144, 0x24)
    game_scene = process.read_memory("int", 0x6A9EC0, 0x768, 0x554C)


def click_seed(seed):
    if isinstance(seed, str):
        if seed in seeds.seeds_string_dict:
            pass
        else:
            raise Exception(f"Unknown seed: {seed}.")
        seed_index = seeds.seeds_string_dict[seed]  # 卡片代号(+48)
        slot_index = seeds.seeds_in_slot[seed_index]  # 该卡片在卡槽中的位置
    else:  # int
        slot_index = seed

    if slot_index is None:
        raise Exception(f"No seed {seeds.seeds_string[seed_index][1]} in slots, operation failed.")

    if slots_count == 10:
        x = 63 + 51 * slot_index
    elif slots_count == 9:
        x = 63 + 52 * slot_index
    elif slots_count == 8:
        x = 61 + 54 * slot_index
    elif slots_count == 7:
        x = 61 + 59 * slot_index
    else:
        x = 61 + 59 * slot_index
    y = 42
    mouse.left_click(x, y)


def click_shovel():
    if slots_count == 10:
        x = 640
    elif slots_count == 9:
        x = 600
    elif slots_count == 8:
        x = 570
    elif slots_count == 7:
        x = 550
    else:
        x = 490
    y = 42
    mouse.left_click(x, y)


def click_grid(*crood):
    if isinstance(crood[0], tuple):
        row, col = crood[0][0], crood[0][1]
    else:
        row, col = crood[0], crood[1]

    x = 80 * col
    if game_scene in (2, 3):
        y = 55 + 85 * row
    elif game_scene in (4, 5):
        if col >= 6:
            y = 45 + 85 * row
        else:
            y = 45 + 85 * row + 20 * (6 - col)
    else:
        y = 40 + 100 * row
    x, y = int(x), int(y)
    mouse.left_click(x, y)
