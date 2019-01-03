#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.

# coding=utf-8

import time
from . import utils

high_precision = False
refresh_time_point = 0


def wait_for_game_start():
    while utils.game_ui() != 3:
        time.sleep(0.01)


def enable_high_precision(on=True):
    global high_precision
    high_precision = on


def thread_sleep_for(time_cs):
    if time_cs > 0.0:
        time.sleep(time_cs / 100)


def delay_a_little_time():
    if high_precision:
        pass
    else:
        thread_sleep_for(0.1)  # 1ms


def game_delay_for(time_cs):
    if time_cs > 0:
        clock = utils.game_clock()
        while (utils.game_clock() - clock) < time_cs:
            delay_a_little_time()


def until_countdown(time_cs, hugewave=False):
    if not hugewave:
        while utils.wave_countdown() > time_cs:
            delay_a_little_time()
    else:
        while utils.wave_countdown() > 4:
            delay_a_little_time()
        while utils.huge_wave_countdown() > time_cs:
            delay_a_little_time()


def until_relative_time_after_refresh(time_relative_cs, wave):
    global refresh_time_point

    while utils.current_wave() < (wave - 1):
        delay_a_little_time()

    huge_wave = wave % 10 == 0
    until_countdown(200, huge_wave)

    clock = utils.game_clock()
    if huge_wave:
        countdown = utils.huge_wave_countdown()
    else:
        countdown = utils.wave_countdown()

    game_delay_for(countdown + time_relative_cs)
    refresh_time_point = clock + countdown


def until_relative_time(time_relative_cs):
    while (utils.game_clock() - refresh_time_point) < time_relative_cs:
        delay_a_little_time()
