import numpy as np
a,b,c = map(float,input("(a,b,c) = ?").split())
arr = [a,b,c]
for i in range(len(arr)-1):
    for j in range(len(arr)-1):
        temp = arr[j+1]
        if arr[j] <= arr[j+1]:
            arr[j+1] = arr[j] 
            arr[j] = temp
        else :
            j += 1
print(arr[0] ,">" , arr[1] , ">" , arr[2])