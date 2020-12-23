from sezi import sezi
from PIL import Image
import time,autopy,pyautogui

region = (0,0,1919,760)
t = (1855,705)  #50
w1 = (1300,310)  #177
w2 = (1460,610)   #99
w3 = (600,510)   #92

# while True:
#     while True:
#         color1 = sezi(region,t)
#         print(color1)
#         if color1 == 50:
#             break
#     if color1 == 50:
#         pyautogui.click(t)
#     else:
#         pass

#     while True:
#         color1 = sezi(region,w1)
#         print(color1)
#         if color1 == 177:
#             break
#     if color1 == 177:
#         pyautogui.click(w2)
#     else:
#         pass

#     while True:
#         color1 = sezi(region,w2)
#         print(color1)
#         if color1 == 99:
#             break
#     if color1 == 99:
#         time.sleep(3)
#         pyautogui.click(w2)
#     else:
#         pass


while True:
    color1 = sezi(region,w3)
    print(color1)
    if color1 == 50:
        break
if color1 == 50:
    pyautogui.click(t)
else:
    pass
