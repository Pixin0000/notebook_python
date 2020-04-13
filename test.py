import numpy as np
import cv2
def main():
    img = cv2.imread("vscode/images/pic03.jpg",-1)
    cv2.imshow("img1",img)
    #img = cv2.resize(img,(nr2,nc2), interpolation= cv2.INTER_NEAREST)
    #scale = input("放大或縮小幾倍")
    img_out = scale_near(img , 1.5)
    cv2.namedWindow("img2",0)
    cv2.resizeWindow("img2",1000,1000)
    cv2.imshow("img2",img_out)
    cv2.waitKey(0)
def scale_near (img ,scale):    
    m= 0
    n = 0
    i = 0
    j = 0
    nr1 , nc1 = img.shape[:2]
    zx = scale
    zy = scale
    nr2 = int(nr1 / scale) 
    nc2 = int(nc1 / scale)
    img_out = np.zeros([nr1,nc1,3],dtype = "uint8")
    for i in range(nr1):
        for j in range(nc1):
            if (i > 0):
                m = int(i/zy + 0.5)
            else:
                m = int(j/zy - 0.5)
            if (j>0):
                n = int(j/zx + 0.5)
            else:
                n = int(j/zx -0.5)
            if((m >= 0) and (m < nr1) and (n >= 0) and (n < nc1)):
                img_out[i][j] = img[m][n]
            else:
                img_out[i][j] = 0
    return img_out
main()