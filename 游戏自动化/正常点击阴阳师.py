import random
import win32api
import time
import win32con
import pyautogui
import win32gui
from PIL import Image
from PIL import ImageGrab
import numpy as np


def Mouse_behavior(x,y,t=0):#鼠标左键点击的函数 x,y:坐标 t:时间
    win32api.SetCursorPos((x,y))#要移动鼠标的坐标
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | 
                         win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0,)#点击鼠标左键
    if t == 0: #t可以自己调数值，也可以随机时间，产生0 到 1之间的随机浮点小数  
        time.sleep(random.random()*2+1)
    else:
        time.sleep(t)
    return 0 

def resoluttion():# 获取屏幕像素分辨率
    return win32api.GetSystemMetrics(0),win32api.GetSystemMetrics(1)

def get_window_info():#获取游戏的窗口坐标
    wdname = u'阴阳师-网易游戏'
    handle = win32gui.FindWindow(0,wdname)# 获取窗口句柄
    if handle == 0:
        return None
    else:
        return win32gui.GetWindowRect(handle)

def get_posx(x,window_size): #返回x相对坐标
    return (window_size[2] - window_size[0]) * x / 870

def get_posy(y,window_size):#返回y相对坐标
    return (window_size[3] - window_size[1]) * y / 520

def guaji():
    i = 0
    t = 0
    while True:
        i += 1
        print(i)
        while True:
            img_zd = ImageGrab.grab((topx + get_posx(780, window_size), topy + get_posy(430, window_size),
                                     topx + get_posx(820, window_size), topy + get_posy(450, window_size)))
            zd_mx = int(topx + get_posx(780,window_size))
            zd_my = int(topy + get_posy(430, window_size))
            img_zd = img_zd.convert('L')
            avg = int(sum(list(img_zd.getdata())) / 256)

            if avg == zd:
                time.sleep(2)
                Mouse_behavior(zd_mx,zd_my,t=0)
                print("战斗开始")
                break
            else:
                time.sleep(5)
                print("等待战斗出现")
                continue
        
        while True:
            img_jl = ImageGrab.grab((topx + get_posx(200, window_size), topy + get_posy(130, window_size),
                                     topx + get_posx(240, window_size), topy + get_posy(150, window_size)))
            jl_mx = int(topx + get_posx(420, window_size))
            jl_my = int(topy + get_posy(430, window_size))
            img_jl = img_jl.convert('L')
            avg = int(sum(list(img_jl.getdata())) / 256)

            if 207 < avg < 220:
                time.sleep(2)
                Mouse_behavior(jl_mx, jl_my, t=0)
                print("奖励出现已点击")
                break
            else:
                time.sleep(1)
                t += 1
                print(t)
                print("等待奖励出现")
                continue
        
        while True:
            img_sl = ImageGrab.grab((topx + get_posx(290, window_size), topy + get_posy(150, window_size),
                                    topx + get_posx(330, window_size), topy + get_posy(170, window_size)))
            sl_mx = int(topx + get_posx(290, window_size))
            sl_my = int(topy + get_posy(150, window_size))
            img_sl = img_sl.convert('L')
            avg = int(sum(list(img_sl.getdata())) / 256)

            if avg == sl:
                time.sleep(2)
                Mouse_behavior(sl_mx, sl_my, t=0)
                print("战斗胜利准备退出")
                break
            else:
                time.sleep(0.5)
                print("等待胜利出现")
                continue




if __name__ == '__main__':
#    Mouse_behavior(1819,736,0) #鼠标左键行为
#    print(pyautogui.position())#利用pyautogui获取鼠标坐标
    print(resoluttion())#获取屏幕分辨率
    print(get_window_info())#获取游戏窗口信息（坐标）
    # 战斗位置 x780，y430， x820，y450 像素513
    # 打完奖励位置 x200,130, x240,y150 像素216
    # 胜利位置 x290,y150, x330,y170 像素534
    zd = 513
    jl = 216
    sl = 543
    window_size = (get_window_info())#获取游戏窗口位置
    topx, topy = window_size[0], window_size[1] #定位起点坐标
    
    # guaji()
    
    # img_zd = ImageGrab.grab((topx + get_posx(200, window_size), topy + get_posy(280, window_size),
    #                         topx + get_posx(280, window_size), topy + get_posy(360, window_size)))
    # img_zd= img_zd.convert('L')
    # avg = int(sum(list(img_zd.getdata())) / 256)
    # img_zd.show()
    # print(avg)
    