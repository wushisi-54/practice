import pyautogui

pyautogui.PAUSE = 1  # 调用在执行动作后暂停的秒数，只能在执行一些pyautogui动作后才能使用，建议用time.sleep
pyautogui.FAILSAFE = True  # 启用自动防故障功能，左上角的坐标为（0，0），将鼠标移到屏幕的左上角，来抛出failSafeException异常

#  判断(x,y)是否在屏幕上
x, y = 122, 244
print(pyautogui.onScreen(x, y))  # 结果为true

width, height = pyautogui.size()  # 屏幕的宽度和高度
print(width, height)
