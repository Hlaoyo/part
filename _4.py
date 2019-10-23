#from params import *
from _3 import *

#对该点落子后的局势进行估分
def getScore(x,y):
    global is_end
    if(ban(x,y)):
        return 0
    if(gameOver(x,y)):
        is_end=False
        return 10000
    score=liveFour(x,y)*1000+(chongFour(x,y)+liveThree(x,y))*100
    for u in range(8):
        if(inBoard(x+dx[u],y+dy[u]) and num[x+dx[u]][y+dy[u]]!=0):
            score=score+1
    return score
#博弈树第一层
def AI1():
    global L1_max
    L1_max=-100000
    if(num[8][8]==0 and go_first==ai):
        return go(8,8)
    keyi=-1; keyj=-1
    for x in [8,7,9,6,10,5,11,4,12,3,13,2,14,1,15,0]:
        for y in [8,7,9,6,10,5,11,4,12,3,13,2,14,1,15,0]:
            if(not downOk(x,y)):
                continue
            num[x][y]=ai
            tempp=getScore(x,y)
            if(tempp==0):
                num[x][y]=0; continue
            if(tempp==10000):
                return go(x,y)
            tempp=AI2()
            num[x][y]=0
            if(tempp>L1_max): #取极大
                L1_max=tempp; keyi=x; keyj=y
    go(keyi,keyj)
#博弈树第二层
def AI2():
    global L2_min
    L2_min=100000
    for x in [8,7,9,6,10,5,11,4,12,3,13,2,14,1,15,0]:
        for y in [8,7,9,6,10,5,11,4,12,3,13,2,14,1,15,0]:
            if(not downOk(x,y)):
                continue
            num[x][y]=3-ai
            tempp=getScore(x,y)
            if(tempp==0):
                num[x][y]=0; continue
            if(tempp==10000):
                num[x][y]=0; return -10000
            tempp=AI3(tempp)
            if(tempp<L1_max): #L1层剪枝
                num[x][y]=0; return -10000
            num[x][y]=0
            if(tempp<L2_min): #取极小
                L2_min=tempp
    return L2_min
#博弈树第三层
def AI3(p2):
    keyp=-100000
    for x in [8,7,9,6,10,5,11,4,12,3,13,2,14,1,15,0]:
        for y in [8,7,9,6,10,5,11,4,12,3,13,2,14,1,15,0]:
            if(not downOk(x,y)):
                continue
            num[x][y]=ai
            tempp=getScore(x,y)
            if(tempp==0):
                num[x][y]=0; continue
            if(tempp==10000):
                num[x][y]=0; return 10000
            if(tempp-p2*2>L2_min): #L2层剪枝
                num[x][y]=0; return 10000
            num[x][y]=0
            if(tempp-p2*2>keyp): #取极大
                keyp=tempp-p2*2
    return keyp