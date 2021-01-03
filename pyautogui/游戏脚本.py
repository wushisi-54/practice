import time,autopy,pyautogui
from PIL import Image
from sezi import sezi

pyautogui.FAILSAFE = True
time.sleep(1)


region=(0,20,1134,672)#窗口位置调整
c = (27,34)#窗口判断
j = (1070,626)#卷轴 33

z = (325,620)#组队 
p = (690,580)#匹配
b = (1024,500) # 准备 = 243
w = (390,150) #完 = 65   败 = 70
w2 = (600,510)    #92
a = 0


#窗口移到固定位置
# autopy.mouse.move(395,200)
# pyautogui.dragTo(0, 20, 1, button='left')
# # currentMouseX, currentMouseY = pyautogui.position()  # 鼠标当前位置
# # print(currentMouseX, currentMouseY)

while a <= 40:
    while True:
        color1 = sezi(region,z)
        print(color1)
        if color1 == 54:
            break
    if color1 == 54:
        time.sleep(2)
        pyautogui.click(z)
        time.sleep(1)
        pyautogui.click(p)
    print("匹配中，请稍等")

    while True:
        color2 = sezi(region,b)
        #print(color2)
        print("等待准备")
        if color2 == 243:
            break
    if color2 ==243:
        pyautogui.click(b)

    while True:
        color3 = sezi(region,w)
        #print(color3)
        print("等待结束")
        if color3 == 65:
            break
        elif color3 == 70:
            break
    if color3 == 65:
        pyautogui.click(w)
        while True:
            color4 = sezi(region,w2)
            print(color4)
            print("等待结算")
            if color4 == 60:
                break
        if color4 == 60:
            time.sleep(5)
            pyautogui.click(w2)
    elif color3 == 70:
        pyautogui.click(w)
    a += 1
    time.sleep(3)



    
# while True:
#     color3 = sezi(region,w2)
#     print(color3)
#     if color3 == 60:
#         break
# if color3 == 60:
#     time.sleep(3)
#     pyautogui.click(w)


