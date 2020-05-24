import sympy as sym
import time
class Differential:
    def dex(self,xpow,time):
        con = 1
        for i in range(time):
            con *= xpow
        x = str(con) + "x^" + str(xpow) 
        return x
    def dx(self,con,x,xpow,pow):
        x_list = list(x)
        x_list.insert(1,"^")
        x_list.insert(2,xpow)
        x = "".join([str(i) for i in x_list])
        time = int(input("幾次微分？"))
        cons = con
        pows = pow
        if(pows >= 1):
            while(time <= pows and time != 0):
                    cons = cons * pows * xpow
                    pows -= 1
                    time -= 1
        elif(pows < 1 ):
            for i in range(time):
                cons = cons * pows * xpow
                pows -= 1
        if(time > pow and pow > 1):
            self.add = print("0")
        else:
            self.add = print("原本為"+ str(con)+"("+str(x)+")"+"^"+str(pow)+","+"微分後為"+str(cons)+"("+str(x)+")"+"^"+str(pows))
    def ex(self,con,xcon,xpow):
            time = int(input("微分幾次"))
            cons = con
            for i in range(time):
                cons *= xpow * xcon
            print("原本為"+str(con)+"e^"+ "(" + str(xcon) + "x^"+str(xpow)+ ")"+","+"後來為"+str(cons)+"x^"+str(time)+"e^"+ "(" + str(xcon)+ "x^" +str(xpow) + ")")
    def inte(self,xcon,sym,xpow,low,max):
        x1 = (xcon/(xpow+1))*max**(xpow+1)
        x2 = (xcon/(xpow+1))*low**(xpow+1)
        x = x1 - x2
        print("原本為"+str(xcon)+str(sym)+"^"+str(xpow)+"後來為"+str(xcon/(xpow+1))+str(sym)+"^"+str(xpow+1)+"="+str(x))
a = Differential()
e = 0
for i in range(0,10):
    for j in range(0,10,-1):
        x = 1
        e += (x**i) / j
        print(j)
        if(j==0):
            i += 1
print(e)
x = sym.symbols('x')
#a.dx(3,"x-12",2,2)
#a.ex(2 , 2 , 2)
a.inte(10,x,2,1,10)
#print(sym.diff(((x-12)/2)**4,x,2)
def num_carry(num,carrys):
    b = -1
    small = num - int(num)
    small_num = [0] * 8
    if small:
        while(small != 0):
            b += 1
            small = small * 2
            if((1 - small)>0):
                small_num[b] = 0
            elif((1 - small)<=0):
                small_num[b] = 1
                small -= 1
            print(small)
        print(small_num)
    a = -1
    arr = [0] * 10
    coe = [0] * 8
    num = int(num)
    for i in range(9,-1,-1):
        for j in range(carrys-1,0,-1):
            if (carrys**i)*j <= num:
                a = a+1
                arr[i] = (carrys**i) * j
                coe[i] = j
                num = num - arr[i]
                i = i-1
                print(num)
            else:
                arr[i] = 0
    print(arr)
    print(coe)
    arr2 = [0] * 8
    for i in range(0,8):
        if coe[i] != 0:
            arr2[i] = coe[i]
    for j in range(0,4):
        temp = arr2[j]
        arr2[j] = arr2[7-j]
        arr2[7-j] = temp
    arr3 = "".join(str(v) for  v in arr2) + "." + "".join(str(v) for v in small_num)
    return arr3
def roam_to_arab(Rome):
    roam = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5,"I": 1}
    #設定羅馬數字對應的數字  
    Rome = list(Rome)
    print(Rome)
    #轉換成list方便存入資料
    sum = 0 
    #總數
    i = 0 
    #迴圈
    j = 0 
    #迴圈
    for i in range(0,len(Rome)-1,2):#每兩個比較
        if(roam[Rome[i]] < roam[Rome[i+1]]):#當後面比較小
            sum += roam[Rome[i+1]] - roam[Rome[i]]
        if(roam[Rome[i+1]] <= roam[Rome[i]]):#當後面的數與前面的數相等或比較大，就都加起來
            print(Rome[i])
            sum += roam[Rome[i+1]] + roam[Rome[i]]
    Rome = "".join(Rome)
    print(str(Rome)+" 換為阿拉伯數字為 "+ str(sum))
def arab_to_roam(num):
    rome_list = []
    while(num != 0):
        if((num//1000)>0):
            for i in range(num//1000):
                rome_list.append("M")
                num -= 1000
        elif((num//900)>0):
            for i in range(num//900):
                rome_list.append("CM")
                num -= 900
        elif((num//500)>0):
            for i in range(num//500):
                rome_list.append("CD")
                num -= 500
        elif((num//400)>0):
            for i in range(num//400):
                rome_list.append("D")
                num -= 400        
        elif((num//100)>0):
            for i in range(num//100):
                rome_list.append("C")
                num -= 100
        elif((num//90)>0):
            for i in range(num//90):
                rome_list.append("XC")
                num -= 100
        elif((num//50)>0):
            for i in range(num//50):
                rome_list.append("L")
                num -= 50
        elif((num//40)>0):
            for i in range(num//40):
                rome_list.append("XL")
                num -= 40
        elif((num//10)>0):
            for i in range(num//10):
                rome_list.append("X")
                num -= 10
        elif((num//9)>0):
            for i in range(num//9):
                rome_list.append("IX")
                num -= 9
        elif((num//5)>0):
            for i in range(num//5):
                rome_list.append("V")
                num -= 5
        elif((num//4)>0):
            for i in range(num//4):
                rome_list.append("IV")
                num -= 4
        elif((num//1)>0):
            for i in range(num//1):
                rome_list.append("I")
                num -= 1
    rome_list = "".join(rome_list)
    # 由array轉為字串
    return rome_list
def main():
    start = time.time()
    roam_to_arab("CMXLIV")
    num = 944
    rome_list = arab_to_roam(num)
    print(str(num)+" 換為羅馬字母為 "+ rome_list)
    carry = num_carry(100.875,8)
    print(str(carry))
    end = time.time()
    #print(end - start)
main()