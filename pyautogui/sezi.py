import pyautogui
from PIL import Image

region=(0,1,1134,653)
a = (1070,626)
def sezi(region,j):
        im = pyautogui.screenshot(region=region)
        im.save('im.png')
        image_raw = Image.open("im.png")
        image_gray = image_raw.convert('L')
        #image_gray.show()
        return image_gray.getpixel(j)
        # c = image_gray.getpixel(j)
        # print(c)

if __name__ == "__main__":
    print(sezi(region,a))