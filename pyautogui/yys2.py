import win32api,win32con,win32gui 
handle = win32gui.FindWindow(0, "阴阳师-网易游戏")#获取窗口句柄
left, top, right, bottom = win32gui.GetWindowRect(handle)#获取窗口位置 左上右下
title = win32gui.GetWindowText(handle)#获取窗口
clsname = win32gui.GetClassName(handle)#获取窗口类名
print(handle)
# print(left,top,right,bottom)
# print(title)
# print(clsname)
# print("%x"%handle)


Hand2 = win32gui.FindWindowEx(handle, None, 'RenderWindow', 'TheRender')
print(Hand2)
