#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.

# coding=utf-8

import time
import ctypes
from . import win32
from . import process

dpi_scale = 1.0


def get_dpi_scale():
    screen = win32.GetDC(None)
    if screen is not None:
        virtual_width = win32.GetDeviceCaps(screen, win32.HORZRES)
        physical_width = win32.GetDeviceCaps(screen, win32.DESKTOPHORZRES)
        win32.ReleaseDC(None, screen)
        scale = physical_width / virtual_width
    else:
        scale = 1.0

    global dpi_scale
    dpi_scale = scale


def MAKELONG(low, high):
    if dpi_scale != 1.0:
        low, high = int(low / dpi_scale), int(high / dpi_scale)
    return ((high & 0xFFFF) << 16) | (low & 0xFFFF)


PVZ_WINDOW_WIDTH = 800
PVZ_WINDOW_HEIGHT = 600


def left_down(x, y):
    coord = MAKELONG(x, y)
    win32.PostMessageW(process.pvz_hwnd, win32.WM_LBUTTONDOWN, win32.MK_LBUTTON, coord)


def left_up(x, y):
    coord = MAKELONG(x, y)
    win32.PostMessageW(process.pvz_hwnd, win32.WM_LBUTTONUP, win32.MK_LBUTTON, coord)


def left_click(x, y):
    coord = MAKELONG(x, y)
    win32.PostMessageW(process.pvz_hwnd, win32.WM_LBUTTONDOWN, win32.MK_LBUTTON, coord)
    win32.PostMessageW(process.pvz_hwnd, win32.WM_LBUTTONUP, win32.MK_LBUTTON, coord)


click = left_click


def right_down(x, y):
    coord = MAKELONG(x, y)
    win32.PostMessageW(process.pvz_hwnd, win32.WM_RBUTTONDOWN, win32.MK_RBUTTON, coord)


def right_up(x, y):
    coord = MAKELONG(x, y)
    win32.PostMessageW(process.pvz_hwnd, win32.WM_RBUTTONUP, win32.MK_RBUTTON, coord)


def right_click(x, y):
    coord = MAKELONG(x, y)
    win32.PostMessageW(process.pvz_hwnd, win32.WM_RBUTTONDOWN, win32.MK_RBUTTON, coord)
    win32.PostMessageW(process.pvz_hwnd, win32.WM_RBUTTONUP, win32.MK_RBUTTON, coord)


def safe_click():
    right_click(0, 0)


def special_button_click(x, y):
    point = win32.POINT()
    win32.GetCursorPos(ctypes.byref(point))
    x_0 = point.x
    y_0 = point.y
    rect = win32.RECT()
    win32.GetWindowRect(process.pvz_hwnd, ctypes.byref(rect))
    border_width = (rect.right - rect.left - PVZ_WINDOW_WIDTH) / 2
    title_height = rect.bottom - rect.top - border_width - PVZ_WINDOW_HEIGHT
    x_1 = int(rect.left + border_width + x)
    y_1 = int(rect.top + title_height + y)
    win32.SetCursorPos(x_1, y_1)
    time.sleep(0.01)
    win32.SetCursorPos(x_1, y_1)
    time.sleep(0.01)
    win32.SetCursorPos(x_1, y_1)

    window_hwnd = win32.WindowFromPoint(point)
    if window_hwnd == process.pvz_hwnd.value:
        left_click(x, y)
        time.sleep(0.01)
    else:
        left_click(x, y)
        time.sleep(0.02)
        left_click(0, 0)

    win32.SetCursorPos(x_0, y_0)
