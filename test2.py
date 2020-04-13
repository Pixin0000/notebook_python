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
img = cv2.imread("images/pic01.jpg",-1)
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