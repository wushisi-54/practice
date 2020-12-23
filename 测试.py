from cv2 import cv2

img = cv2.imread(r"E:/img/pig.png") #读入图片,后面带下列三个参数
# '''
# cv2.IMREAD_COLOR：默认参数，读入一副彩色图片，忽略alpha通道
# cv2.IMREAD_GRAYSCALE：读入灰度图片
# cv2.IMREAD_UNCHANGED：顾名思义，读入完整图片，包括alpha通道
# '''
# #调颜色
# '''
# cv2.cvtColor(图片，颜色选择)
# '''
# img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
# cv2.namedWindow("pig") #设置窗口名称（仅限英文，中文会乱码）
# cv2.imshow("pig",img) #显示图像（'窗口名字'，图片）
# cv2.waitKey(0) #暂停窗口
# cv2.destroyAllWindows()

duibi = cv2.CascadeClassifier(r"E:/img/pig.png")
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
duibis = duibi.detectMultiScale(gray)
print(duibis)