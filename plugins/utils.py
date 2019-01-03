#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.


from . import process


def game_on():
    if process.is_valid():
        return True
    else:
        return process.find_pvz_1051()


def game_mode():
    return process.read_memory("int", 0x6A9EC0, 0x7F8)


def game_ui():
    return process.read_memory("int", 0x6A9EC0, 0x7FC)


def game_scene():
    return process.read_memory("int", 0x6A9EC0, 0x768, 0x554C)


def game_paused():
    return process.read_memory("bool", 0x6A9EC0, 0x768, 0x164)


def mouse_in_game():
    return process.read_memory("bool", 0x6A9EC0, 0x768, 0x59)


def mouse_have_something():
    return process.read_memory("int", 0x6A9EC0, 0x768, 0x138, 0x30) in (1, 6, 8)


def game_clock():
    return process.read_memory("int", 0x6A9EC0, 0x768, 0x5568)


def wave_countdown():
    return process.read_memory("int", 0x6A9EC0, 0x768, 0x559C)


def huge_wave_countdown():
    return process.read_memory("int", 0x6A9EC0, 0x768, 0x55A4)


def current_wave():
    return process.read_memory("int", 0x6A9EC0, 0x768, 0x557C)


def dance_clock():
    return process.read_memory("int", 0x6A9EC0, 0x838)