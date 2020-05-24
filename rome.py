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
            print("前比後小"+str(sum))
        if(roam[Rome[i+1]] <= roam[Rome[i]]):#當後面的數與前面的數相等或比較大，就都加起來
            print(Rome[i])
            sum += roam[Rome[i+1]] + roam[Rome[i]]
            print("後比前小"+str(sum))
    Rome = "".join(Rome)
    print(str(Rome)+" 換為阿拉伯數字為 "+ str(sum))
def arab_to_roam(num):
    rome_list = []
    while(num):
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
    return rome_list
def main():
    roam_to_arab("CMXLIV")
    num = 944
    rome_list = arab_to_roam(num)
    rome_list = "".join(rome_list)
    print(str(num)+" 換為羅馬字母為 "+ rome_list)
main()

