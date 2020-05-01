
from matplotlib import pyplot as plt

from matplotlib import animation

from matplotlib.font_manager import FontProperties

import math

g = 9.8

fig = plt.figure()

ax= fig.add_subplot(111)

ax.set_aspect('equal')

#中文字體路徑 設置


#獲取一個列表，有205個間隔數據，每個數據間隔0.005

def get_intervals(u, theta):

    intervals = []

    start = 0

    interval = 0.005

    while start < t_flight:

        intervals.append(start)

        start = start + interval

    return intervals

#更新時間間隔參數，從而不斷改變圓的圓心坐標位置，讓其移動

def update(t):

    x = u*math.cos(theta_radians)*t

    y = u*math.sin(theta_radians)*t - 0.5*g*t*t

    circle.center = x, y

    return circle,

#產生時間間隔參數，（從0,0.005,0.01一直到1.02 ）依次傳遞給updata函數

def generate():

    for t in intervals:

        yield t

def Print():

    print ("初始速度（米/秒）:",u)

    print ("發射角度（度）",theta)

    print ("飛行總時間（秒）",t_flight)

    print ("飛行距離（米）",xmax)

#初始參數，u為初始速度，theta為發射角度

u = 30

theta =60

#返回一個角度的弧度值

theta_radians = math.radians(theta)

'''

Out[65]: 0.5235987755982988

'''

#飛彈飛行總時間，運用導數知識可以求得公式

t_flight = 2*u*math.sin(theta_radians)/g

intervals = get_intervals(u, theta_radians)

'''

[0,

0.005,

0.01,

0.015,

0.02,

0.025,

0.10500000000000002,

0.11000000000000003,

0.11500000000000003,

.......

0.9900000000000008,

0.9950000000000008,

1.0000000000000007,

1.0050000000000006,

1.0100000000000005,

1.0150000000000003,

1.0200000000000002]

len(intervals)

Out[67]: 205

'''

xmin = 0

#x橫軸最大距離

xmax = u*math.cos(theta_radians)*intervals[-1]

ymin = 0

t_max = u*math.sin(theta_radians)/g

#y橫軸最大距離

#ymax = u*math.sin(theta)*t_max - 0.5*g*t_max**2

ymax =xmax

#設置坐標軸的x,y取值範圍

ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, ymax))

#創建一個圓，圓點在（0,0），半徑為0.2

circle = plt.Circle((xmin, ymin), 2)

ax.add_patch(circle)

#動畫函數，讓炮彈不斷變化，generate產生數據傳遞給update更新

anim = animation.FuncAnimation(fig, update,generate,interval=5)

plt.title(u'飛彈發射軌跡')

plt.xlabel(u'水平距離(米)')

plt.ylabel(u'飛彈運行高度（米）')

plt.show()
