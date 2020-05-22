def temp_distance(seventh,temp_dict):
    tem_distance = []
    # 設定一個串列存入第7筆資料與溫度的距離
    for i in temp_dict.keys():
        temp_gap = (seventh - temp_dict[i])
    # 計算第七個人與每個人溫度的距離
        tem_distance.append(temp_gap)
    # 插入串列
    return tem_distance #回傳值
def humid_distance(seventh,hum_dict):
    hum_distance = [] 
    # 設定一串列存入與每筆資料溼度的距離
    for i in hum_dict.keys():
        hum_gap = (seventh - hum_dict[i]) #與第7筆資料的距離
        hum_distance.append(hum_gap)#插入函式中
    return hum_distance # 回傳
def distance(tem_distance,humid_distance):
    distance_list1 = []
    # 設定一串列存入與每個人的距離
    distance_list2 = []
    # 設定一串列存入排序後的距離
    for i in range(0,len(tem_distance)):
        distance_list1.append((humid_distance[i]**2 + tem_distance[i]**2)**0.5)
        #考慮溫度跟溼度計算距離並存入
    distance_list2 = distance_list1[:]
        #複製第一個串列
    for j in range(len(distance_list2)):#氣泡排序第二個串列
        for k in range(0,len(distance_list2)-1):
            temp = distance_list2[k+1]
            if  distance_list2[k+1] <= distance_list2[k]:
                distance_list2[k+1] = distance_list2[k]
                distance_list2[k] = temp
    return distance_list1,distance_list2 #回傳串列1及串列2
def decision(distance_list1,distance_list2,rating):
    top_three = [] # 設定一個list存入距離最小的人在原本的位置
    top_three_rating = [] # 設定一個list存入top_three中每個人的滿意度
    sum = 0 # 定義總數 
    print("與每筆數據原距離為",distance_list1) 
    print("每筆數據排序過後為",distance_list2)
    k = 3 # 取的數量
    for i in range(k):
        top_three.append(distance_list1.index(distance_list2[i])+1)
        #去原串列中尋找排序後串列的值的位置(+1後代表第幾筆資料)
    for i in range(k):
        top_three_rating.append(rating[top_three[i]])
        #把資料帶入滿意度字典中並把鍵值存入串列中
    for j in range(k):
        sum += top_three_rating[j]
    print("最近的前"+str(k)+"人為",top_three)
    print("前"+str(k)+"人的滿意度",top_three_rating)
    if(sum<0):#判斷式 判斷總數為正或負
        print("因為sum="+ str(sum) +"所以可以推斷第七位為不滿意")
    elif(sum>0):
        print("因為sum= "+ str(sum) +"所以可以推斷第七位為滿意")
    else:
        print("無法判斷")
def main():
    seventh_temp = 127 
    # 第七個烤箱溫度
    seventh_hum = 23 
    # 第七個烤箱溼度
    temp_dict = {"first":123 , "second":126,"third":124,"fourth":122,"fifth":124,"sixth":122}
    # 設定字典中每個人的烤箱溫度
    hum_dict = {"first":23 , "second":23,"third":25,"fourth":23,"fifth":26,"sixth":22}
    # 設定字典中每個人的烤箱溼度
    rating = { 1:1 , 2:-1 , 3:-1 , 4:1 , 5:-1 , 6:1}
    # 設定字典中每個人的評價
    tem_distance = temp_distance(seventh_temp,temp_dict)
    # 傳入函式中計算溫度的差值
    hum_distance = humid_distance(seventh_hum,hum_dict)
    # 傳入函式中計算溼度的差值
    distance_list1,distance_list2 = distance(tem_distance,hum_distance)
    # 傳入函式中計算距離並且回傳未排序及排序過的距離
    decision(distance_list1,distance_list2,rating)
    # 最後透過排序過的距離去看滿意跟不滿意的次數並下判斷
main()
