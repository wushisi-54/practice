# import pyautogui,time
# #防止鼠标不受控制(移到四个角落就行)
# pyautogui.FAILSAFE = True
# time.sleep(3)
# while True:
#     #截图
#     region=(185,487,322,27)
#     im = pyautogui.screenshot(region=region)
#     #im.save('im.png')
#     #获取图片颜色
#     for i in range(40,300,80):
#         px = im.getpixel((i,10))
#         print(px)
#         #判断颜色
#         if px[0] == 2:
#             pyautogui.click(region[0] + i,region[1] + 10)

# #写病毒
# f = open(r'文件名字','rb')#二进制打开'rb'
# content = f.read()
# length = len(content)/2
# f.close()
# f = open(r'文件名字','wb')#二进制打开'wb'
# f.seek(int(length))
# f.write('ssafw214'.encode())
# f.close()