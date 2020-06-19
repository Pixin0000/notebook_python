import cv2 
import numpy as np
def main():
    img = cv2.imread("images\Lenna_Salt_Pepper.jpg",0)
    #讀取圖片
    cv2.imshow("origin",img)
    #show原圖
    nr,nc = img.shape[0:2]
    #切分圖片的高度與寬度
    element = int(input("要濾幾*幾濾波?"))
    #看要濾幾*幾的濾波
    arr = np.zeros((element,element))
    #設置一矩陣儲存資料
    arr2 = np.zeros(element**2)
    #設一矩陣用來排列
    for down in range(0,nr-element+1):#高度 
        for right in range(0,nc-element+1):#寬度 
            for i in range(0,element):
                for j in range(0,element):
                    arr[i][j] =  img[i+down][j+right]
                    #使其可往右捲及往下掃描
            arr2 = arr.flatten() #轉為一維矩陣以便排列大小
            arr2.sort()#排列大小
            middle = (element**2)//2 #中間元素的位子
            add(element,nr,nc,down,right,img,arr2[middle])#取中間值傳入函式中
def add(element,nr,nc,down,right,img,middle):
    img[down][right] = middle #把中間的值輸入進新圖片中
    if(down == nr-element and right == nc-element):#因為for迴圈的問題所以減掉element代表執行完最後的元素位子
        show(img)#傳入印出圖片的函式中
def show(img):
    cv2.imshow("after",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
main()