import win32api,win32con,win32gui ,time,win32ui
from PIL import Image 



def doClick(cx,cy): #后台点击
    long_position = win32api.MAKELONG(cx,cy)
    win32api.SendMessage(hwnd,win32con.WM_LBUTTONDOWN,win32con.MK_LBUTTON, long_position)
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP,win32con.MK_LBUTTON, long_position)
    print(cx,cy)

def window_capture(hwnd): #后台截图 应用窗口全部并保存
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
    im_PIL_TEMP.save("暂时存放.png")
    mfcDC.DeleteDC()
    saveDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)
    return im_PIL_TEMP

def crop_img(img,x1,y1,x2,y2,):#截图之后获取一个值
    im = Image.open(img)
    crop_img = im.crop((x1, y1, x2, y2))
    img_l = crop_img.convert('L')
    avg = sum(list(img_l.getdata()))
    return avg

def jiaoben():
    while 999:
        while 1:
            avg = crop_img(img, 1042, 576, 1076, 600)
            window_capture(hwnd)
            if avg == 68642:
                time.sleep(0.5)
                print("战斗出现已点击")
                print(avg)
                doClick(1060, 566)
                break
            else:
                time.sleep(1)
                print(avg)
                continue
        while 1:
            avg = crop_img(img, 348, 111, 374, 137)
            window_capture(hwnd)
            if avg == 15062:
                time.sleep(0.5)
                print("奖励出现已点击")
                print(avg)
                doClick(548,540)
                break
            else:
                time.sleep(1)
                print(avg)
                continue
        while 1:
            avg = crop_img(img, 727, 161, 737, 170)
            window_capture(hwnd)
            if avg == 21222:
                time.sleep(0.5)
                print("胜利出现已点击")
                print(avg)
                doClick(496,523)
                break
            else:
                time.sleep(1)
                print(avg)
                continue

if __name__ == '__main__':
    #战斗的位置 1042,576,1076,600 值：68642
    #奖励的位置 348,111,374,137 值：15062
    #胜利的位置 727,161,737,170 值：21222
    hwnd = win32gui.FindWindow(0, "阴阳师-网易游戏")  # 获取窗口句柄
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)  # 获取窗口位置 左上右下
    title = win32gui.GetWindowText(hwnd)  # 获取窗口
    clsname = win32gui.GetClassName(hwnd)  # 获取窗口类名
    img = "F:/practice/暂时存放.png"

    
    # print(hwnd)
    # print(left,top,right,bottom)
    # print(title)
    # print(clsname)
    # print("%x"%hwnd)
    # doClick(1060,566)
    # im = crop_img(img,1042,576,1076,600)
    # im.save("裁剪之后.png")
    # get_hash(im)
    # img_l = im.convert('L')
    # img_l.show()
    # avg = sum(list(img_l.getdata())) 
    # print(crop_img(img, 348, 111, 374, 137))
    jiaoben()
    