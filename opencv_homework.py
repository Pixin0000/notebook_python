import cv2 
import numpy as np
def main():
    img = cv2.imread("images\Butterfly_pepper.jpg",0)
    #img = cv2.imread("images\salt_lenna.jpg",0) 
    #讀取圖片
    cv2.imshow("origin",img)
    #show原圖
    nr,nc = img.shape[0:2]
    #取得圖的寬與高度
    arr = np.zeros((3,3))
    #設置一矩陣儲存3*3的資料
    arr2 = np.zeros(9)
    #設一矩陣用來排列
    for down in range(0,nr-2):#3*3的方格向下移1格
        for right in range(0,nc-2):#3*3的方格向右移1格
            for i in range(0,3):
                for j in range(0,3):
                    arr[i][j] = img[i+down][j+right]
                    #使其可往右捲及往下掃描
            arr2 = arr.flatten() #轉為一維矩陣
            arr2.sort()#排列大小
            add(nr,nc,down,right,img,arr2[4])#取中間值傳入函式中
def add(nr,nc,i,j,img,middle):
    img[i][j] = middle #把中間的值存入一變數
    '''
    print("img["+str(i)+"]"+"["+str(j)+"]"+"=",img[i][j])
    #印出每筆資料
    '''
    if(i == nr-3 and j == nc-3):#因掃描的為3*3 所以最後需要-3
        show(img)#傳入印出圖片的函式中
def show(img):
    img_RGB = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.imshow("after_blur",img_RGB)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
main()