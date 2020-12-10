from PIL import Image
'''
#保存图片
im = ImageGrab.grab()
im.save("000.png")
'''
img = "D:/pythonxm/practice/000.png"
im = Image.open(img)

print(type(im))