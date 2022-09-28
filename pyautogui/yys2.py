import win32api,win32con,win32gui ,time,random,win32ui
from PIL import Image 


def Mouse_behavior(x, y, t=0):  # 鼠标左键点击的函数 x,y:坐标 t:时间
    win32api.SetCursorPos((x, y))  # 要移动鼠标的坐标
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
                         win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0,)  # 点击鼠标左键
    if t == 0:  # t可以自己调数值，也可以随机时间，产生0 到 1之间的随机浮点小数
        time.sleep(random.random()*2+1)
    else:
        time.sleep(t)
    return 0

def doClick(cx,cy): #后台点击
    long_position = win32api.MAKELONG(cx,cy)
    win32api.SendMessage(hwnd,win32con.WM_LBUTTONDOWN,win32con.MK_LBUTTON, long_position)
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP,win32con.MK_LBUTTON, long_position)
    print(cx,cy)

hwnd = win32gui.FindWindow(0, "阴阳师-网易游戏")#获取窗口句柄
left, top, right, bottom = win32gui.GetWindowRect(hwnd)#获取窗口位置 左上右下
title = win32gui.GetWindowText(hwnd)#获取窗口
clsname = win32gui.GetClassName(hwnd)#获取窗口类名


def window_capture(hwnd): #后台截图 应用窗口全部
    w = right - left
    h = bottom - top
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    im_PIL_TEMP = Image.frombuffer(
        'RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)
    win32gui.DeleteObject(saveBitMap.GetHandle())
    mfcDC.DeleteDC()
    saveDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)
    return im_PIL_TEMP

# print(hwnd)
# print(left,top,right,bottom)
# print(title)
# print(clsname)
# print("%x"%hwnd)
# doClick(1060,566)
# window_capture(hwnd).show()