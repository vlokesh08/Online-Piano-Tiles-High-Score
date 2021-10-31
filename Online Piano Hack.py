from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(1355, 630)[0] == 0:
        click(1355, 630)
    if pyautogui.pixel(1450, 630)[0] ==0:
        click(1450, 630)
    if pyautogui.pixel(1520, 630)[0] == 0 :
        click(1520, 630)
    if pyautogui.pixel(1610, 630)[0] == 0 :
        click(1610, 630)
