import cv2
import numpy as np 
import matplotlib.pyplot as plt
def main():
    input_img = cv2.imread("images/car.jpg",-1)
    #讀入汽車圖片
    trans_img = transform(input_img)
    #取出車牌的部份圖形
    grad_img = laplacian(trans_img,2)
    #使用梯度讓車牌輪廓更明顯
    gray_img = cvt_gray(trans_img)
    #轉換為灰階
    black_white_img = devided(gray_img)
    #二值化
    blur_img = blur(black_white_img)
    #濾波器
    nr,nc = gray_img.shape[:2]
    #取出長與寬
    histogram(nr,nc,blur_img)
    #二階取樣
    cv2.imshow("car_origin",input_img)
    #show 原始圖 
    cv2.imshow("after_trans",trans_img)
    #show 翻轉圖
    cv2.imshow("gray_pic",gray_img)
    #show 灰階圖
    cv2.imshow("grad", grad_img)
    # show 梯度圖
    cv2.imshow("blur",blur_img)
    canny_img = cv2.Canny(trans_img,100,150)
    cv2.imshow("canny",canny_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def transform(input_img):#轉為正面
    pts1 = np.float32([[212,320],[220,465],[545,485],[560,330]])
    #車牌區間
    pts2 = np.float32([[0,0],[0,500],[650,500],[650,0]])
    #視窗尺寸
    T = cv2.getPerspectiveTransform(pts1,pts2)
    trans_img = cv2.warpPerspective(input_img,T,(650,500))
    return trans_img
def cvt_gray(img2):#
    img3 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    return img3
def blur(img3):
    img3 = cv2.GaussianBlur(img3,(7,7),0)
    for i in range(0,1000):
        img3 = cv2.medianBlur(img3,5)
        #中值取樣
    return img3
def laplacian(img3,num):
    kernal = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    sobelx = np.array([[-1,-2,1],[0,0,0],[1,2,1]])
    sobely = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    gradx = cv2.filter2D(img3,cv2.CV_32F,sobelx)
    grady = cv2.filter2D(img3,cv2.CV_32F,sobely)
    if(num == 1):
        gx = abs(gradx)
        g = np.uint8(np.clip(gx,0,255))
        return g
    if(num == 2):
        gy = abs(grady)
        g = np.uint8(np.clip(gy,0,255))
        return g
    if(num == 3):#拉普拉斯
        temp = cv2.filter2D(img3,cv2.CV_32F,kernal) + 128
        g = np.uint8(np.clip(temp,0,255))
        return g
    else:
        g = abs(gradx) + abs(grady)
        return g
def histogram(nr,nc,img3):
    i = 0
    j = 0
    hist = np.zeros([256])
    for i in range(nr): 
        for j in range(nc):
            x = img3[i][j]
            if img3[i][j] != 255 and img3[i][j] != 0:
                img3[i][j] = 255
            else:
                hist[x] += 1
    plt.xlim([0,256])
    plt.stem(hist)
    plt.show()
    #img3 = cv2.equalizeHist(img3)
    '''
    for k in range(len(hist)):
         if hist[k] < 2000 and hist[k] > 0:
             for i in range(nr):
                 for j in range(nc):
                    if(img3[i][j] == hist[k]):
                        print(i,j)
                        img3[i][j] = 0
    '''
    return img3
def devided(img3):#二值化
    nr,nc = img3.shape[:2]
    for i in range(0,nr):
        for j in range(0,nc):
            if(img3[i][j] >= 128): 
                img3[i][j] = 255
            elif(img3[i][j] < 128):
                img3[i][j] = 0
    return img3
main()
