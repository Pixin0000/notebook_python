import matplotlib.pyplot as plt
import numpy as np
import cv2
# plt.rcParams['Dejavu Sans']=['Microsoft JhengHei']
# file encoding: utf-8 
''' 
    x = np.arange(-180,180)
    a = np.array([-100,100])
    b = np.array([2,2])
    y = x**2
    y2 = 2*x
    plt.xlim(-180,180)
    plt.ylim(0,100)
    plt.plot(x,y)
    plt.plot(a,b)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("Characteristic curve of Diode" )
    plt.plot(x,y2,linestyle="dashed",linewidth=0.5,color="red",marker=".")
    plt.show()
    plt.savefig("filename.png",dpi=300,format="png")
'''
'''
plt.title("homework" )
x = np.array([0 ,5 ,10	,15	,20	,25	,30	,35	,40	,45	,50,55,60
,65,70,75,80,85,90,95,100,105,110,115,120,125])
y = np.array([0,4.07	,6.35,	7.65,	8.61	,9.14	,9.48	,9.7	,9.83,	9.91	,9.96
,10.01	,10.04,	10.06	,10.06	,10.07
])
i = np.array([1,0.584	,0.365	,0.237,	0.155	,0.096	,0.06	,0.035	,0.024	,
0.016	,0.011 , 0.0076	,0.005	,0.004	,0.003	,0.002,	0.002	,0.001,	0.001	,
0.001	,0.001 ,0.001	,0.001	,0.001,	0])
a = [1,2,4,3,2,1,2,1]
x = [1,2,4,3,2,1,2,1]
n = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
y = np.zeros(16)
def average(t1,t2):
    return float((t1+t2) / 2)
j = 0
i = 0
plt.figure(0)
plt.plot(n[:len(a)],a[:],"r")
for index in range(len(a)-1):
    ave = average(a[j],a[j+1])
    print("ave = " , ave)
    a.insert(j+1,ave) # [1 , 2 , 3 ]   --> [1 , 3 , 2 , 3]
    print(j)
    j+= 2
plt.figure(1)
plt.stem(n[:len(a)],a)
i = 0
plt.figure(2)
for i in range(len(x)*2):
    y[i] = x[int(i/2)]
plt.stem(n[:len(y)],y,"y")
plt.ylim(0,6)
plt.show()
'''
import numpy as np
import cv2
def main():
    img1 = cv2.imread("images/pic02.jpg",-1)
    cv2.imshow("img1",img1)
main()