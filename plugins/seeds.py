#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.

# coding=utf-8

"""
Seeds
"""

import time
import functools

from . import process
from . import mouse

seeds_string = [
    ["Peashooter", "豌豆射手", "豌豆", "单发"],
    ["Sunflower", "向日葵", "小向", "花"],
    ["Cherry Bomb", "樱桃炸弹", "樱桃", "炸弹", "爆炸", "草莓", "樱"],
    ["Wall-nut", "坚果墙", "坚果", "墙果", "柠檬圆"],
    ["Potato Mine", "土豆雷", "土豆", "地雷", "土豆地雷"],
    ["Snow Pea", "寒冰射手", "冰豆", "冰豌豆", "雪花豌豆", "雪花"],
    ["Chomper", "大嘴花", "大嘴", "食人花", "食"],
    ["Repeater", "双发射手", "双发", "双发豌豆"],
    ["Puff-shroom", "小喷菇", "小喷", "喷汽蘑菇", "免费蘑菇", "炮灰菇", "小蘑菇", "免费货", "免费"],
    ["Sun-shroom", "阳光菇", "阳光", "阳光蘑菇"],
    ["Fume-shroom", "大喷菇", "大喷", "烟雾蘑菇", "大蘑菇", "喷子", "喷"],
    ["Grave Buster", "墓碑吞噬者", "墓碑", "墓碑苔藓", "苔藓", "咬咬碑"],
    ["Hypno-shroom", "魅惑菇", "魅惑", "迷惑菇", "催眠蘑菇", "催眠", "花蘑菇", "毒蘑菇"],
    ["Scaredy-shroom", "胆小菇", "胆小", "胆怯蘑菇", "胆小鬼蘑菇", "杠子蘑菇"],
    ["Ice-shroom", "寒冰菇", "冰菇", "冷冻蘑菇", "冰蘑菇", "面瘫", "蓝冰", "原版冰", "冰"],
    ["Doom-shroom", "毁灭菇", "核蘑菇", "核弹", "核武", "毁灭", "末日蘑菇", "末日菇", "末日", "黑核", "原版核", "核"],
    ["Lily Pad", "睡莲", "荷叶", "莲叶"],
    ["Squash", "窝瓜", "倭瓜", "窝瓜大叔", "倭瓜大叔", "镇压者"],
    ["Threepeater", "三线射手", "三线", "三头豌豆", "三头", "三管", "管"],
    ["Tangle Kelp", "缠绕海草", "海草", "缠绕海藻", "海藻", "毛线"],
    ["Jalapeno", "火爆辣椒", "辣椒", "墨西哥胡椒", "辣", "椒"],
    ["Spikeweed", "地刺", "刺", "尖刺", "尖刺杂草", "棘草"],
    ["Torchwood", "火炬树桩", "火树", "火炬", "树桩", "火炬木", "火"],
    ["Tall-nut", "高坚果", "搞基果", "高建国", "巨大墙果", "巨大", "高墙果", "大土豆"],
    ["Sea-shroom", "海蘑菇", "水兵菇"],
    ["Plantern", "路灯花", "灯笼", "路灯", "灯笼草", "灯笼花", "吐槽灯", "灯"],
    ["Cactus", "仙人掌", "小仙", "掌"],
    ["Blover", "三叶草", "三叶", "风扇", "吹风", "愤青"],
    ["Split Pea", "裂荚射手", "裂荚", "双头", "分裂豌豆", "双头豌豆"],
    ["Starfruit", "杨桃", "星星", "星星果", "五角星", "1437", "大帝", "桃"],
    ["Pumpkin", "南瓜头", "南瓜", "南瓜罩", "套"],
    ["Magnet-shroom", "磁力菇", "磁铁", "磁力蘑菇", "磁"],
    ["Cabbage-pult", "卷心菜投手", "包菜", "卷心菜", "卷心菜投抛者"],
    ["Flower Pot", "花盆", "盆"],
    ["Kernel-pult", "玉米投手", "玉米", "黄油投手", "玉米投抛者"],
    ["Coffee Bean", "咖啡豆", "咖啡", "兴奋剂", "春药"],
    ["Garlic", "大蒜", "蒜"],
    ["Umbrella Leaf", "叶子保护伞", "莴苣", "白菜", "保护伞", "伞叶", "叶子", "伞", "叶"],
    ["Marigold", "金盏花", "金盏草", "金盏菊", "吐钱花"],
    ["Melon-pult", "西瓜投手", "西瓜", "绿皮瓜", "瓜", "西瓜投抛者"],
    ["Gatling Pea", "机枪射手", "机枪", "加特林豌豆", "加特林", "格林豌豆", "枪"],
    ["Twin Sunflower", "双子向日葵", "双子", "双向", "双花"],
    ["Gloom-shroom", "忧郁蘑菇", "忧郁", "忧郁菇", "章鱼", "曾哥", "曾哥蘑菇", "曾"],
    ["Cattail", "香蒲", "猫尾草", "猫尾", "猫尾香蒲", "小猫", "猫"],
    ["Winter Melon", "冰瓜", "冰西瓜", "冰冻西瓜"],
    ["Gold Magnet", "吸金磁", "吸金", "吸金草", "金磁铁"],
    ["Spikerock", "地刺王", "钢刺", "钢地刺", "尖刺岩石", "石荆棘"],
    ["Cob Cannon", "玉米加农炮", "玉米炮", "加农炮", "春哥", "春哥炮", "炮", "春", "神"],
]
seeds_imitater_string = ["Imitater", "模仿者", "模仿", "复制", "白", "小白", "变身茄子"]
seeds_string_dict = {}
for i, items in enumerate(seeds_string):
    for item in items:
        seeds_string_dict[item] = i
        for j, im in enumerate(seeds_imitater_string):
            seeds_string_dict[im + item] = i + 48
            seeds_string_dict[im + " " + item] = i + 48
seeds_list = []
seeds_in_slot = [None] * (48 * 2)


def update_seeds_list():
    global seeds_list, seeds_in_slot
    seeds_list = []
    slots_count = process.read_memory("int", 0x6A9EC0, 0x768, 0x144, 0x24)
    slots_offset = process.read_memory("unsigned int", 0x6A9EC0, 0x768, 0x144)
    for i in range(slots_count):
        seed_type = process.read_memory("int", slots_offset + 0x5C + i * 0x50)
        seed_imitater_type = process.read_memory("int", slots_offset + 0x60 + i * 0x50)
        if seed_type == 48:
            row, col = divmod(seed_imitater_type, 8)
            imitater = True
        else:
            row, col = divmod(seed_type, 8)
            imitater = False
        seed = row + 1, col + 1, imitater
        seeds_list.append(seed)

    seeds_in_slot = [None] * (48 * 2)
    for index, seed in enumerate(seeds_list):
        row, col, imitater = seed
        i = (row - 1) * 8 + (col - 1) + (48 if imitater else 0)
        seeds_in_slot[i] = index + 1


SEED_0_0_X = 50
SEED_0_0_Y = 160
IMITATER_SEED_0_0_X = 215
IMITATER_SEED_0_0_Y = 160
SEED_WIDTH = 50
SEED_HEIGHT = 70
IMITATER_X = 490
IMITATER_Y = 550


def select_seed_by_crood(row, col, imitater=False):
    if imitater:
        if row not in (1, 2, 3, 4, 5):
            raise Exception("'row' out of range.")
        if col not in (1, 2, 3, 4, 5, 6, 7, 8):
            raise Exception("'col' out of range.")
    else:
        if row not in (1, 2, 3, 4, 5, 6):
            raise Exception("'row' out of range.")
        if col not in (1, 2, 3, 4, 5, 6, 7, 8):
            raise Exception("'col' out of range.")

    if imitater:
        mouse.special_button_click(IMITATER_X, IMITATER_Y)
        time.sleep(0.3)
        x = IMITATER_SEED_0_0_X + (col - 1) * (SEED_WIDTH + 1)
        y = IMITATER_SEED_0_0_Y + (row - 1) * (SEED_HEIGHT + 2)
    else:
        x = SEED_0_0_X + (col - 1) * (SEED_WIDTH + 3)
        y = SEED_0_0_Y + (row - 1) * (SEED_HEIGHT + 0)
    mouse.left_click(x, y)
    time.sleep(0.2)


@functools.singledispatch
def seed_to_crood(seed):
    raise Exception(f"Unknown seed type {type(seed)}.")


@seed_to_crood.register(int)
def _(seed):
    if seed == 1437:
        row = 4
        col = 6
        imitater = False
    else:
        imitater = seed >= 48
        index = seed % 48
        row, col = divmod(index, 8)
    return row + 1, col + 1, imitater


@seed_to_crood.register(tuple)
def _(seed):
    if len(seed) == 2:
        row, col = seed
        imitater = False
    elif len(seed) == 3:
        row, col, im = seed
        imitater = im not in (False, 0)
    return row, col, imitater


@seed_to_crood.register(str)
def _(seed):
    if not seed in seeds_string_dict:
        raise Exception(f"Unknown seed: {seed}.")
    seed_index = seeds_string_dict[seed]  # 卡片代号(+48)
    imitater = seed_index >= 48
    index = seed_index % 48
    row, col = divmod(index, 8)
    return row + 1, col + 1, imitater


def select_all_seeds(seeds_selected=None):
    default_seeds = [40, 41, 42, 43, 44, 45, 46, 47, 8, 8 + 48]
    slots_count = process.read_memory("int", 0x6A9EC0, 0x768, 0x144, 0x24)
    if seeds_selected is None:
        seeds_selected = default_seeds[0:slots_count]
    while len(seeds_selected) < slots_count:
        for seed in default_seeds:
            if seed_to_crood(seed) not in [seed_to_crood(s) for s in seeds_selected]:
                seeds_selected += [seed]
                break
    if len(seeds_selected) != slots_count:
        raise Exception(f"Seeds count {len(seeds_selected)} != slots count {slots_count}.")
    seeds_selected = [seed_to_crood(seed) for seed in seeds_selected]

    while process.read_memory("int", 0x6A9EC0, 0x774, 0xD24) < slots_count:
        for _ in range(10):
            mouse.left_click(108, 42)
            time.sleep(0.1)
        time.sleep(0.25)
        for seed in seeds_selected:
            row, col, imitater = seed
            select_seed_by_crood(row, col, imitater)
        time.sleep(0.75)
