class Differential():
    def __init__(self,x):#初始化
        self.x = x
    def dx(self,xcon,xpow,equation_pow,time):#微分
        x_list = list(self.x) #轉換為list
        x_list.insert(1,"^") #插入次方符號
        x_list.insert(2,xpow) #插入次方數
        x1 = "".join([str(i) for i in x_list])#原本的函式轉成文字
        cons = xcon #微分後的系數
        pows = xpow #微分後的x次方數
        equation_pows = equation_pow #後來方程式次方數
        origin_time = time
        if(equation_pows > 1):#當方程式次方數大於1
            for i in range(time):
                # 套入微分一次的公式算出係數
                cons = cons * equation_pows * xpow 
                equation_pows -= 1 
                time -= 1
        elif(equation_pows < 1 ):#當方程式次方數小於1
            for i in range(time):
                cons = cons * pows * equation_pows #微分係數公式
                equation_pows -= 1
                #當方程式次方數小於1時會少了time-=1
        elif(equation_pows == 1):
            for i in range(time):
                cons = cons * pows * equation_pow
                pows -= 1
                equation_pows = 1
                #當方程式次方數等於1時意即只有x的次方數會變動
        x_after = list(self.x)#新的函式
        x_after.insert(1,"^")#插入次方符號
        x_after.insert(2,pows)#插入新的次方數
        x2 = "".join([str(i) for i in x_after])#轉成文字
        if(origin_time > equation_pow and equation_pow > 1): #當次數大於函式的次方數時會變成0
            print("0")
        elif(origin_time == equation_pow and equation_pow > 1):
            print("原本為"+ str(xcon)+"("+str(x1)+")"+"^"+str(equation_pow)+","+"微分後為"+str(cons))#次數一樣則為常數
        else:
            print("原本為"+ str(xcon)+"("+str(x1)+")"+"^"+str(equation_pow)+","+"微分後為"+str(cons)+"("+str(x2)+")"+"^"+str(equation_pows))
    def unassign_inte(self,xcon,xpow):#不定積分
        cons = xcon/(xpow+1)#積分後的係數
        pows = xpow + 1 #積分後的次方數
        print("原本為"+str(xcon)+str(self.x)+"^"+str(xpow)+"後來為"+str(cons)+str(self.x)+"^"+str(pows))
    def assign_inte(self,xcon,xpow,max,low):#定積分
        x1 = (xcon/(xpow+1))*max**(xpow+1)#次方數加一，常數除以次方數加一再帶入上限
        x2 = (xcon/(xpow+1))*low**(xpow+1)#次方數加一，常數除以次方數加一再帶入下限
        x = x1 - x2#上限減下限
        cons = xcon/(xpow+1)#積分後的係數
        pows = xpow + 1 #積分後的次方數
        print("原本為"+str(xcon)+str(self.x)+"^"+str(xpow)+"定積分後為"+str(x))
def num_carry(num,carrys):
    carrys_16 = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    #設定16進位符號代表的值
    origin = num
    b = -1 #定義array位置格子數
    small = num - int(num) #小數部分
    small_num = [0] * 8
    if small:#當小數有值
        while(small != 0):
            b += 1#array位置往前加1格，一開始即為0的位置
            small = small * carrys #每次乘上進位的數值
            if((small - int(small))>=0 and int(small) != 0):#當小數不為整數時
                small_num[b] = int(small) #取出整數部分
                small -= int(small)#減掉整數部分
            elif((small - int(small))<1):#當整數沒有值時
                small_num[b] = 0#不取出繼續迴圈
    arr = [0] * 10 #定義格數
    coe = [0] * 10 #紀錄常數
    num = int(num)
    for i in range(9,-1,-1):#位置從大的數回來
        for j in range(carrys-1,0,-1):#係數也從大的數回來
            if (carrys**i)*j <= num: #配對找到小於num的最大的組合
                arr[i] = (carrys**i) * j#加入剛剛的值
                if(j >= 10):
                    coe[i] = carrys_16[j]
                else:
                    coe[i] = j
                num = num - arr[i]#減掉加入的值
                i = i-1
            else:
                arr[i] = 0
    for j in range(0,5):
        temp = coe[j]
        coe[j] = coe[9-j]#交換位置，因為剛剛是從後面數回來，因此位置會相反
        coe[9-j] = temp
    if (origin - int(origin)) > 0:#當有小數時
        arr3 = "".join(str(v) for v in coe) + "." + "".join(str(v) for v in small_num)
        print(str(origin)+"轉換為"+str(carrys)+"進位後為"+(arr3))
    else:#當沒有小數時
        arr4 = "".join(str(v) for v in coe)
        print(str(origin)+"轉換為"+str(carrys)+"進位後為"+(arr4))
def roam_to_arab(Rome):
    roam = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5,"I": 1}
    #設定羅馬數字對應的數字  
    Rome = list(Rome)
    #轉換成list方便存入資料
    sum = 0 
    #總數
    i = 0 
    j = 0 
    for i in range(0,len(Rome)-1,2):#每兩個字符比較
        if(roam[Rome[i]] < roam[Rome[i+1]]):#當後面的數值比較大
            sum += roam[Rome[i+1]] - roam[Rome[i]]#後減前ex.IV = 4
        if(roam[Rome[i+1]] <= roam[Rome[i]]):#當前面的數與後面的數相等或比較大，就都加起來
            sum += roam[Rome[i+1]] + roam[Rome[i]]#後加前ex.CC = 200
    if((len(Rome)%2) > 0):#當長度為奇數時最後一個字符會沒加到，因此針對這個情況再設定一次
        if(roam[Rome[len(Rome)-2]] < roam[Rome[len(Rome)-1]]):#當後面的數值比較大
            sum += roam[Rome[len(Rome)-1]] - roam[Rome[len(Rome)-2]] - roam[Rome[len(Rome)-2]]#後減前ex.IV = 4
        elif(roam[Rome[len(Rome)-2]] >= roam[Rome[len(Rome)-1]]):#當前面的數與後面的數相等或比較大，就都加起來
            sum += roam[Rome[len(Rome)-1]]
    Rome = "".join(Rome)#轉換成字符
    print(str(Rome)+" 換為阿拉伯數字為 "+ str(sum))
def arab_to_roam(num):
    arab = num
    rome_list = [] #創建一個list
    while(num != 0):
        #一層一層切分，並把字符由大到小加入list中，直到num=0
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
                rome_list.append("D")
                num -= 500
        elif((num//400)>0):
            for i in range(num//400):
                rome_list.append("CD")
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
    print(rome_list)
    # 由array轉為字串
    print(str(arab)+" 換為羅馬字母為 "+ rome_list)
def decide():
    print("------------------")
    print("1. roam to arab   ")#羅馬數字到阿拉伯數字
    print("2. arab to roam   ")#阿拉伯數字到羅馬數字
    print("3. num to carry   ")#十進位看要轉換成幾進位
    print("4. differential   ")#簡單的微分
    print("5. integral       ")#簡單的積分
    print("q. quit           ")#退出
    print("r. return to list ")
    print("------------------") 
    function = input("要使用甚麼功能呢?")
    if function == '1':
        roam = input("請輸入羅馬數字")
        if roam == 'r':#若為r則重新執行程式
            decide()
        roam_to_arab(roam) 
    elif function == '2':
        arab = input("請輸入阿拉伯數字")
        if arab == 'r':
            decide()
        else:
            arab = int(arab)
            arab_to_roam(arab)
    elif function == '3':
        num = input("請輸入數字")
        if num == 'r':
            decide()
        else:
            num = float(num)
        carry = input("請輸入幾進位")
        if carry == 'r':
            decide()
        else:
            carry = int(carry)
            num_carry(num,carry)
    elif function == '4':
        equation = Differential('x')
        xcon = float(input("x係數？"))
        xpow = float(input("x幾次方？"))
        equation_pow = float(input("方程式次方？"))
        time = int(input("幾次微分？"))
        equation.dx(xcon,xpow,equation_pow,time)
    elif function == '5':
        equation = Differential('x')
        xcon = xcon = int(input("x係數？"))
        xpow = int(input("x幾次方？"))
        num = input("1. 不定積分　2.定積分 ")
        if(num == '1'):
            equation.unassign_inte(xcon,xpow)
        elif(num == '2'):
            max = int(input("請輸入上限"))
            low = int(input("請輸入下限"))
            equation.assign_inte(xcon,xpow,max,low)
        elif(num == 'r'):
            decide()
        else:
            print("請輸入正確的數值")
    elif function == 'q':
        print("quit...") #退出
    elif function == 'r':
        decide() #重新執行
    else:
        print("請輸入有效字符")
def main():
    function = decide()
    #進入函式中決定欲執行的選項
main()