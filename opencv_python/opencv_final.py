import cv2
import numpy as np 
import pytesseract
def main():
    input_img = cv2.imread("images/car.jpg",-1)
    #讀入汽車圖片
    trans_img = transform(input_img)
    #取出車牌的部份圖形
    gray_img = cvt_gray(trans_img)
    #轉換為灰階去二值化
    grad_img = laplacian(gray_img,1)
    #使用梯度讓車牌輪廓更明顯
    blur_img = blur(gray_img)
    #濾波器濾掉雜質
    black_white_img = devided(blur_img)
    #二值化
    nohole_img = hole_filling(black_white_img)
    #去除白色破洞
    canny_img = cv2.Canny(nohole_img,30,100)
    #取出線條
    cv2.imshow("car_origin",input_img)
    #show 原始圖 
    cv2.imshow("after_trans",trans_img)
    #show 翻轉圖
    cv2.imshow("grad", grad_img)
    # show 梯度圖
    cv2.imshow("blur",blur_img)
    # show 濾波圖
    cv2.imshow("nohole",nohole_img)
    #show補漏洞圖
    cv2.imshow("black",black_white_img)
    #show二值化後的圖
    cv2.imshow("canny",canny_img)
    #show線條圖
    retain_num(canny_img)
    #移除圖片雜質
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def transform(input_img):#轉為正面
    x1,y1 = 212,320
    x2,y2 = 220,465
    x3,y3 = 545,485
    x4,y4 = 560,330
    pts1 = np.float32([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])
    #車牌區間
    pts2 = np.float32([[0,0],[0,500],[650,500],[650,0]])
    #視窗尺寸
    T = cv2.getPerspectiveTransform(pts1,pts2)
    #由1轉換為2
    trans_img = cv2.warpPerspective(input_img,T,(650,500))
    return trans_img
def cvt_gray(trans_img):
    gray_img = cv2.cvtColor(trans_img,cv2.COLOR_BGR2GRAY)
    #轉換為灰階
    text = pytesseract.image_to_string(gray_img,lang="eng")
    print(text)
    return gray_img
def blur(nohole_img):
    for i in range(0,1000):
        blur_img = cv2.medianBlur(nohole_img,3)
    #中值濾波去除雜訊
    return blur_img
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
def devided(gray_img):#二值化
    nr,nc = gray_img.shape[:2]
    for i in range(0,nr):
        for j in range(0,nc):
            if(gray_img[i][j] >= 128): 
               gray_img[i][j] = 255
            elif(gray_img[i][j] < 128):
                gray_img[i][j] = 0
    return gray_img
def hole_filling(img):
    kernal = np.ones((3,3),np.uint8)#創kernal
    g = cv2.erode(img,kernal,iterations=3)#侵蝕
    return g
def retain_num(img):
    g = img.copy()
    nr , nc = img.shape[:2]
    negative = 255 - img
    n,labels = cv2.connectedComponents(negative)
    for x in range(nr):
        for y in range(nc):
            if labels[x,y] == 0:#若為白色
               if(x<=110 or x>=440):#只取得介於110~440之間的值
                    g[x,y] = 0
    cv2.imshow("final_img",g)
    devide(g)
def devide(img):
    nr,nc = img[:2]
    point1 = (0,0)
    point2 = (107,500)
    img1 = img[point1[1]:point2[1] , point1[0]:point2[0]]
    point1 = (107,0)
    point2 = (218,500)
    img2 = img[point1[1]:point2[1] , point1[0]:point2[0]]
    point1 = (218,0)
    point2 = (308,500)
    img3 = img[point1[1]:point2[1] , point1[0]:point2[0]]
    point1 = (321,0)
    point2 = (427,500)
    img4 = img[point1[1]:point2[1] , point1[0]:point2[0]]
    point1 = (455,0)
    point2 = (530,500)
    img5 = img[point1[1]:point2[1] , point1[0]:point2[0]]
    point1 = (558,0)
    point2 = (648,500)
    img6 = img[point1[1]:point2[1] , point1[0]:point2[0]]
    cv2.imshow("img1",img1)
    cv2.imshow("img2",img2)
    cv2.imshow("img3",img3)
    cv2.imshow("img4",img4)
    cv2.imshow("img5",img5)
    cv2.imshow("img6",img6)
main()