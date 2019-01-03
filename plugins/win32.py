#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.

"""
Windows API
"""

import ctypes
from ctypes import c_size_t as size_t
from ctypes.wintypes import BOOL
from ctypes.wintypes import DWORD
from ctypes.wintypes import INT
from ctypes.wintypes import UINT
from ctypes.wintypes import LONG
from ctypes.wintypes import HWND
from ctypes.wintypes import HANDLE
from ctypes.wintypes import HDC
from ctypes.wintypes import LPVOID
from ctypes.wintypes import LPCVOID
from ctypes.wintypes import LPCWSTR
from ctypes.wintypes import LPDWORD
from ctypes.wintypes import POINT
from ctypes.wintypes import LPPOINT
from ctypes.wintypes import LPRECT
from ctypes.wintypes import WPARAM
from ctypes.wintypes import LPARAM
from ctypes.wintypes import RECT


class SecurityAttributes(ctypes.Structure):
    _fields_ = [("nLength", DWORD), ("lpSecurityDescriptor", LPVOID), ("bInheritHandle", BOOL)]


LPSECURITY_ATTRIBUTES = ctypes.POINTER(SecurityAttributes)
LPTHREAD_START_ROUTINE = ctypes.WINFUNCTYPE(DWORD, LPVOID)


PROCESS_ALL_ACCESS = 0x001F0FFF

STILL_ACTIVE = 0x00000103

TIMERR_NOERROR = 0

MEM_COMMIT = 0x00001000
MEM_RELEASE = 0x00008000
PAGE_EXECUTE_READWRITE = 0x40
INFINITE = 0xFFFFFFFF

WM_LBUTTONDOWN = 0x0201
WM_LBUTTONUP = 0x0202
WM_RBUTTONDOWN = 0x0204
WM_RBUTTONUP = 0x0205

MK_LBUTTON = 0x0001
MK_RBUTTON = 0x0002

WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101

VK_ESCAPE = 0x1B
VK_SPACE = 0x20

VK_LEFT = 0x25
VK_UP = 0x26
VK_RIGHT = 0x27
VK_DOWN = 0x28

REALTIME_PRIORITY_CLASS = 0x00000100
HIGH_PRIORITY_CLASS = 0x00000080
ABOVE_NORMAL_PRIORITY_CLASS = 0x00008000
NORMAL_PRIORITY_CLASS = 0x00000020
BELOW_NORMAL_PRIORITY_CLASS = 0x00004000
IDLE_PRIORITY_CLASS = 0x00000040

HORZRES = 8
DESKTOPHORZRES = 118


user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32
winmm = ctypes.windll.winmm
gdi32 = ctypes.windll.gdi32
MessageBoxW = user32.MessageBoxW
MessageBoxW.argtypes = [HWND, LPCWSTR, LPCWSTR, UINT]
MessageBoxW.restype = INT
FindWindowW = user32.FindWindowW
FindWindowW.argtypes = [LPCWSTR, LPCWSTR]
FindWindowW.restype = HWND
GetWindowThreadProcessId = user32.GetWindowThreadProcessId
GetWindowThreadProcessId.argtypes = [HWND, LPDWORD]
GetWindowThreadProcessId.restype = DWORD
OpenProcess = kernel32.OpenProcess
OpenProcess.argtypes = [DWORD, BOOL, DWORD]
OpenProcess.restype = HANDLE
GetExitCodeProcess = kernel32.GetExitCodeProcess
GetExitCodeProcess.argtypes = [HANDLE, LPDWORD]
GetExitCodeProcess.restype = BOOL
CloseHandle = kernel32.CloseHandle
CloseHandle.argtypes = [HANDLE]
CloseHandle.restype = BOOL
ReadProcessMemory = kernel32.ReadProcessMemory
ReadProcessMemory.argtypes = [HANDLE, LPCVOID, LPVOID, size_t, LPDWORD]
ReadProcessMemory.restype = BOOL
WriteProcessMemory = kernel32.WriteProcessMemory
WriteProcessMemory.argtypes = [HANDLE, LPVOID, LPCVOID, size_t, LPDWORD]
WriteProcessMemory.restype = BOOL
VirtualAllocEx = kernel32.VirtualAllocEx
VirtualAllocEx.argtypes = [HANDLE, LPVOID, size_t, DWORD, DWORD]
VirtualAllocEx.restype = LPVOID
VirtualFreeEx = kernel32.VirtualFreeEx
VirtualFreeEx.argtypes = [HANDLE, LPVOID, size_t, DWORD]
VirtualFreeEx.restype = BOOL
CreateRemoteThread = kernel32.CreateRemoteThread
CreateRemoteThread.argtypes = [HANDLE, LPSECURITY_ATTRIBUTES, size_t, LPTHREAD_START_ROUTINE, LPVOID, DWORD, LPDWORD]
CreateRemoteThread.restype = HANDLE
WaitForSingleObject = kernel32.WaitForSingleObject
WaitForSingleObject.argtypes = [HANDLE, DWORD]
WaitForSingleObject.restype = DWORD
GetLastError = kernel32.GetLastError
GetLastError.argtypes = []
GetLastError.restype = DWORD
timeBeginPeriod = winmm.timeBeginPeriod
timeBeginPeriod.argtypes = [UINT]
timeBeginPeriod.restype = UINT
timeEndPeriod = winmm.timeEndPeriod
timeEndPeriod.argtypes = [UINT]
timeEndPeriod.restype = UINT
WindowFromPoint = user32.WindowFromPoint
WindowFromPoint.argtypes = [POINT]
WindowFromPoint.restype = HWND
GetWindowRect = user32.GetWindowRect
GetWindowRect.argtypes = [HWND, LPRECT]
GetWindowRect.restype = BOOL
GetCursorPos = user32.GetCursorPos
GetCursorPos.argtypes = [LPPOINT]
GetCursorPos.restype = BOOL
SetCursorPos = user32.SetCursorPos
SetCursorPos.argtypes = [INT, INT]
SetCursorPos.restype = BOOL
SendMessageW = user32.SendMessageW
SendMessageW.argtypes = [HWND, UINT, WPARAM, LPARAM]
SendMessageW.restype = LONG
PostMessageW = user32.PostMessageW
PostMessageW.argtypes = [HWND, UINT, WPARAM, LPARAM]
PostMessageW.restype = BOOL
GetCurrentProcess = kernel32.GetCurrentProcess
GetCurrentProcess.argtypes = []
GetCurrentProcess.restype = HANDLE
GetPriorityClass = kernel32.GetPriorityClass
GetPriorityClass.argtypes = [HANDLE]
GetPriorityClass.restype = DWORD
SetPriorityClass = kernel32.SetPriorityClass
SetPriorityClass.argtypes = [HANDLE, DWORD]
SetPriorityClass.restype = BOOL
GetDC = user32.GetDC
GetDC.argtypes = [HWND]
GetDC.restype = HDC
GetDeviceCaps = gdi32.GetDeviceCaps
GetDeviceCaps.argtypes = [HDC, INT]
GetDeviceCaps.restype = INT
ReleaseDC = user32.ReleaseDC
ReleaseDC.argtypes = [HWND, HDC]
ReleaseDC.restype = INT
