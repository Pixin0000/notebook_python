import cv2
import matplotlib.pyplot as plt
img = cv2.imread("images/pic01.jpg" , -1)
cv2.namedWindow("ex1",0)
cv2.resizeWindow("ex1",550,550)
cv2.imshow("ex1", img)
#!!!!!! 不加沒辦法運行
cv2.waitKey(0)
cv2.destroyAllWindows()
#!!!!!! 