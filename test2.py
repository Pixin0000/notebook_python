import numpy as np 
import matplotlib.pyplot as plt 
import cv2
'''
img = cv2.imread("images/pic01.jpg", -1)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.namedWindow("img", -1)
zeros = np.zeros(img.shape[0:2] , dtype = "uint8")
r,g,b = cv2.split(img)
cv2.resizeWindow("example", 640 , 480)
cv2.imshow("Red", cv2.merge([zeros,zeros,r]))
cv2.imshow("Green", cv2.merge([zeros,g,zeros]))
cv2.imshow("Blue", cv2.merge([b,zeros,zeros]))
plt.imshow(img)
plt.show()
'''
'''
img = cv2.imread("images/pic03.jpg",-1)
cv2.namedWindow("example",0)
cv2.resizeWindow("example",640,480) 
cv2.rectangle(img,(540,300),(700,400),(255,0,0),4)
cv2.imshow("example",img)
img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
plt.figure()
plt.imshow(img)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
import matplotlib.pyplot as plt
def main():
    img = cv2.imread("images/lenna.jpeg",0)
    nr , nc = img.shape[:2]
    cv2.imshow("asd", img)
    #histogram(nr , nc)
def histogram(nr,nc):
    i = 0
    j = 0
    hist = np.zeros([256])
    for i in nr:
        for j in nc:
            x = img[i][j]
            hist[x] = hist[x] + 1
    plt.plot(hist)
    plt.xlim([0,256])
main()
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt
def main():
    img1 = cv2.imread("images/lenna.jpg",-1)
    nr , nc = img1.shape[:2]
    cv2.imshow("asd", img1)
    histogram(nr , nc , img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def histogram(nr,nc,img1):
    i = 0
    j = 0
    hist = np.zeros([256])
    for i in range(nr):
        for j in range(nc):
            x = img1[i][j]
            hist[x] += 1
    plt.plot(hist)
    plt.xlim([0,256])
    plt.show()
main()