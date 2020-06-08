import cv2
import numpy as np
def transform(input_img):#轉為正面
    x1,y1 = 212,320
    x2,y2 = 220,465
    x3,y3 = 545,485
    x4,y4 = 560,330
    #取得車牌的4點
    pts1 = np.float32([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])
    #車牌區間
    pts2 = np.float32([[0,0],[0,500],[650,500],[650,0]])
    #設定轉置後的座標
    T = cv2.getPerspectiveTransform(pts1,pts2)
    trans_img = cv2.warpPerspective(input_img,T,(650,500))
    return trans_img
def cvt_gray(trans_img):
    gray_img = cv2.cvtColor(trans_img,cv2.COLOR_BGR2GRAY)
    #轉換為灰階
    return gray_img
def blur(black_white_img):
    names = locals()
    #定義local變數
    names["img%s" %0] = black_white_img
    #定義第一張圖
    for i in range(1,100):
        names["img%s" %i] = cv2.medianBlur(names["img%s" %(i-1)],3)
        #看要做濾波幾次 
    blur_img = cv2.medianBlur(names['img99'],3)
    return blur_img
def Sobel_gradient( gray_img, direction = 1 ):
	sobel_x = np.array( [ [-1,-2,-1], [ 0, 0, 0], [ 1, 2, 1] ] )
	sobel_y = np.array( [ [-1, 0, 1], [-2, 0, 2], [-1, 0, 1] ] )
	if direction == 1:
		grad_x = cv2.filter2D( gray_img, cv2.CV_32F, sobel_x )
		gx = abs( grad_x )
		g = np.uint8( np.clip( gx, 0, 255 ) )
        #梯度 x
	elif direction == 2:
		grad_y = cv2.filter2D( gray_img, cv2.CV_32F, sobel_y )
		gy = abs( grad_y )
		g = np.uint8( np.clip( gy, 0, 255 ) )
        #梯度y
	else:
		grad_x = cv2.filter2D( gray_img, cv2.CV_32F, sobel_x )
		grad_y = cv2.filter2D( gray_img, cv2.CV_32F, sobel_y )
		magnitude = abs( grad_x ) + abs( grad_y )
		g = np.uint8( np.clip( magnitude, 0, 255 ) )
	return g
def devided(gray_img):#二值化
    nr,nc = gray_img.shape[:2]
    #取出高與寬
    black_white_img = gray_img.copy()
    #複製原圖
    for i in range(0,nr):
        for j in range(0,nc):
            if(gray_img[i][j] >= 128): 
                black_white_img[i][j] = 255
            elif(gray_img[i][j] < 128):
                black_white_img[i][j] = 0
    #分化兩值
    return black_white_img
def hole_filling(img):
    kernal = np.ones((3,3),np.uint8)#創kernal
    g = cv2.erode(img,kernal,iterations=1)#侵蝕
    return g
def getHProjection(img):
    hProjection = np.zeros(img.shape,np.uint8)
    #圖像高與寬
    (h,w)=img.shape
    #取出高與寬 
    arr = []
    h_ = [0]*h
    for y in range(h):
        for x in range(w):
            if img[y,x] == 255:
                h_[y]+=1
    #循環統計每一行像素的白色點個數
    for y in range(h):
        for x in range(h_[y]):
            hProjection[y,x] = 255
    #繪製水平投影圖像
    for i in range(h):
        if h_[i] < 10:#當一行中的白點個數少於10時代表可能是斷層
            arr.append(i)
    print(arr)
    for i in range(len(arr)-1):
        if (arr[i+1]-arr[i])>=300:#因車牌字符差不多高為300pixel
            point1 = (0,arr[i])
            point2 = (650,arr[i+1])
            img = img[point1[1]:point2[1] , point1[0]:point2[0]]
    cv2.imshow('hProjection',hProjection)
    #show 橫圖
    return img
def getVProjection(image):
    names = locals()
    arr = []
    vProjection = np.zeros(image.shape,np.uint8)
    #圖像高與寬
    (h,w) = image.shape
    #取出長與寬
    w_ = [0]*w
    for x in range(w):
        for y in range(h):
            if image[y,x] == 255:
                w_[x]+=1
    #循環統計每一列的白色個數
    for x in range(w):
        for y in range(h-w_[x],h):
            vProjection[y,x] = 255
    #繪製垂直投影圖像
    for i in range(w):
        if w_[i] ==0 or i == w-1:
            arr.append(i)
        #去切分全部黑色的部份    
    print(arr)
    for i in range(len(arr)-1):
        if (arr[i+1]-arr[i])>=50:#當兩個黑色間距>=50代表隔了一個字母
            point1 = (arr[i],0)
            point2 = (arr[i+1],500)
            names['x%s' %i] = image[point1[1]:point2[1] , point1[0]:point2[0]]
            #得出每一塊字符
            cv2.imshow("img"+ str(i),names['x' + str(i)])
    cv2.imshow('vProjection',vProjection)
    #show v圖
    return image
def main():
    input_img = cv2.imread("images/car.jpg",-1)
    #讀入汽車圖片
    trans_img = transform(input_img)
    #取出車牌的部份圖形
    gray_img = cvt_gray(trans_img)
    #轉換為灰階去二值化
    grad_img = Sobel_gradient(gray_img,3)
    #使用梯度讓車牌輪廓更明顯
    black_white_img = devided(grad_img)
    #二值化
    blur_img = blur(black_white_img)
    #濾波器濾掉雜質
    nohole_img = hole_filling(blur_img)
    #去除白色破洞
    canny_img = cv2.Canny(nohole_img,30,100)
    #找出線條
    himage = getHProjection(canny_img)
    #水平切切出文字
    yimage = getVProjection(himage)
    #垂直切分割文字
    cv2.imshow("car_origin",input_img)
    #show 原始圖 
    cv2.imshow("after_trans",trans_img)
    #show 翻轉圖
    cv2.imshow("gray_pic",gray_img)
    #show 灰度圖
    cv2.imshow("grad_pic", grad_img)
    # show 梯度圖
    cv2.imshow("blur_pic",blur_img)
    # show 濾波圖
    cv2.imshow("nohole_pic",nohole_img)
    #show補漏洞圖
    cv2.imshow("black_white_pic",black_white_img)
    #show二值化後的圖
    cv2.imshow("canny_pic",canny_img)
    #show線條圖
    cv2.imshow("himage",himage)
    #移除圖片雜質
    cv2.waitKey(0)
    cv2.destroyAllWindows()
main()