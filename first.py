import cv2
img = cv2.imread("images\Butterfly_pepper.jpg",0)
img2 = cv2.imwrite("pepper_butterfly.jpg",img)
#讀取圖片
print(img[0][0])
cv2.imshow("origin",img)
img = cv2.medianBlur(img,3)
cv2.imshow("after",img)
#show原圖
nr,nc = img.shape[0:2]
print(nr,nc)
cv2.waitKey(0)
cv2.destroyAllWindows()