import cv2
import numpy as np
from matplotlib import pyplot as plt
def plot_demo(image):
    plt.hist(image.ravel(),256,[0,256])#histSize参数表示灰度级的个数,ranges参数表示像素值的范围，通常[0,256]
    # numpy的ravel函数功能是将多维数组降为一维数组
    plt.show()
img = cv2.imread("/Users/lenovo/PycharmProjects/zhifangtu/girl.jpg",1)
img=cv2.resize(img,(512,512),interpolation=cv2.INTER_CUBIC)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #opencv的直方图均衡化要基于单通道灰度图像
cv2.imshow("01",gray)
plot_demo(gray)
dst=cv2.equalizeHist(gray) #自动调整图像对比度，把图像变得更清晰
cv2.imshow("02",dst)
plot_demo(dst)
cv2.waitKey (0)
cv2.destroyAllWindows()
