#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.

# coding=utf-8

"""
Process / Memory
"""

import ctypes
import struct
from . import win32

pvz_hwnd = win32.HWND()
pvz_pid = win32.DWORD()
pvz_handle = win32.HANDLE()
cpp_typename = {
    "char": "b",
    "bool": "?",
    "unsigned char": "B",
    "short": "h",
    "unsigned short": "H",
    "int": "i",
    "unsigned int": "I",
    "long": "l",
    "unsigned long": "L",
    "long long": "q",
    "unsigned long long": "Q",
    "float": "f",
    "double": "d",
}


def is_valid():
    if pvz_handle.value is None:
        return False
    exit_code = win32.DWORD()
    win32.GetExitCodeProcess(pvz_handle, ctypes.byref(exit_code))
    return exit_code.value == win32.STILL_ACTIVE


def read_memory(data_type, *address, array=1):
    level = len(address)
    offset = ctypes.c_void_p()
    buffer = ctypes.c_uint()

    for i in range(level):
        offset.value = buffer.value + address[i]

        if i != level - 1:
            win32.ReadProcessMemory(pvz_handle, offset, ctypes.byref(buffer), 4, None)
        else:
            fmt_str = "<" + str(array) + cpp_typename[data_type]
            size = struct.calcsize(fmt_str)
            buff = ctypes.create_string_buffer(size)
            win32.ReadProcessMemory(pvz_handle, offset, buff, size, None)
            if array == 1:
                result = struct.unpack(fmt_str, buff.raw)[0]
            else:
                result = struct.unpack(fmt_str, buff.raw)
    return result


def write_memory(data_type, values, *address):
    level = len(address)
    offset = ctypes.c_void_p()
    buffer = ctypes.c_uint()

    for i in range(level):
        offset.value = buffer.value + address[i]

        if i != level - 1:
            win32.ReadProcessMemory(pvz_handle, offset, ctypes.byref(buffer), 4, None)
        else:
            if not isinstance(values, (tuple, list)):
                values = [values]
            array = len(values)
            fmt_str = "<" + str(array) + cpp_typename[data_type]
            size = struct.calcsize(fmt_str)
            buff = ctypes.create_string_buffer(size)
            buff = struct.pack(fmt_str, *values)
            win32.WriteProcessMemory(pvz_handle, offset, buff, size, None)


def open_process_by_window(class_name, window_name):
    global pvz_hwnd, pvz_pid, pvz_handle
    if is_valid():
        win32.CloseHandle(pvz_handle)
    pvz_hwnd.value = None
    pvz_pid.value = 0
    pvz_handle.value = None
    pvz_hwnd.value = win32.FindWindowW(class_name, window_name)
    if pvz_hwnd.value is not None:
        win32.GetWindowThreadProcessId(pvz_hwnd, ctypes.byref(pvz_pid))
    if pvz_pid.value != 0:
        pvz_handle.value = win32.OpenProcess(win32.PROCESS_ALL_ACCESS, False, pvz_pid)
    result = pvz_handle.value is not None
    return result


def find_pvz_1051():
    open_process_by_window("MainWindow", "植物大战僵尸中文版")
    return True
