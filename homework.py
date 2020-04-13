import numpy as np
def main():
    x1 , y1 = map(float , input("(x1 , y1) : ").split()) #第1個點座標切分兩個值分到兩個變數,float
    x2 , y2 = map(float , input("(x2 , y2) : ").split()) #第2個點座標切分兩個值分到兩個變數,float
    x = x1 - x2 #x軸距離
    y = y1 - y2 #y軸距離
    print("距離為",distance(x,y))
def distance(x,y):
    return np.sqrt( x ** 2 + y ** 2 )
main()
'''
def main():
   feet , inch =  map(int,input("幾呎幾吋？").split()) #分別把呎跟寸存到變數中
   print(switch(feet , inch),"公分")#調用函式計算
def switch(feet , inch):
    centimeter = 0 #定義變數
    while (feet > 0): #當呎不為0
        inch += 12 #把呎轉換為吋
        feet -= 1
    centimeter = 2.54 * inch #轉換完帶入公式
    return centimeter
main() #調用主函式
'''
3
'''
one = 20 #定義單個價錢
number = int(input("要買幾個?")) #輸入幾個
price = 0 #定義總價
if(number%12): #當number != 12
    price = number * x
else :
    price = number / 12 * 200 #等於12時 看有幾打再*上200
int(price) #取整
print(price)
'''