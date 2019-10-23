from graphics import *
import time
# from themain import *
from part2 import *

# dx = [1,1,0,-1,-1,-1,0,1] #x,y方向向量
# dy = [0,1,1,1,0,-1,-1,-1]
# # num = [[0 for a in range(16)] for a in range(16)]
# go_first = 1 #先手标志

#在给定的方向v(v区分正负)上，和该点同色棋子的个数
def numInline(x,y,v):
    i=x+dx[v]; j=y+dy[v]
    s=0; ref=num[x][y]
    if(ref==0): return 0
    while(sameColor(i,j,ref)):
        s=s+1; i=i+dx[v]; j=j+dy[v]
    return s
#该点四个方向里(即v不区分正负)，活四局势的个数
def liveFour(x,y):
    key=num[x][y]; s=0
    for u in range(4):
        samekey=1
        samekey,i=numofSamekey(x,y,u,1,key,samekey)
        if(not downOk(x+dx[u]*i,y+dy[u]*i)):
            continue
        samekey,i=numofSamekey(x,y,u,-1,key,samekey)
        if(not downOk(x+dx[u]*i,y+dy[u]*i)):
            continue
        if(samekey==4):
            s=s+1
    return s
#该点八个方向里(即v区分正负)，冲四局势的个数
def chongFour(x,y):
    key=num[x][y]; s=0
    for u in range(8):
        samekey=0; flag=True; i=1
        while(sameColor(x+dx[u]*i,y+dy[u]*i,key) or flag):
            if(not sameColor(x+dx[u]*i,y+dy[u]*i,key)):
                if(flag and inBoard(x+dx[u]*i,y+dy[u]*i) and num[x+dx[u]*i][y+dy[u]*i]!=0):
                    samekey-=10
                flag=False
            samekey+=1
            i+=1
        i-=1
        if(not inBoard(x+dx[u]*i,y+dy[u]*i)):
            continue
        samekey,i=numofSamekey(x,y,u,-1,key,samekey)
        if(samekey==4):
            s+=1
    return s-liveFour(x,y)*2
#该点四个方向里活三，以及八个方向里断三的个数
def liveThree(x,y):
    key=num[x][y]; s=0
    for u in range(4):
        samekey=1
        samekey,i=numofSamekey(x,y,u,1,key,samekey)
        if(not downOk(x+dx[u]*i,y+dy[u]*i)):
            continue
        if(not downOk(x+dx[u]*(i+1),y+dy[u]*(i+1))):
            continue
        samekey,i=numofSamekey(x,y,u,-1,key,samekey)
        if(not downOk(x+dx[u]*i,y+dy[u]*i)):
            continue
        if(not downOk(x+dx[u]*(i-1),y+dy[u]*(i-1))):
            continue
        if(samekey==3):
            s+=1
    for u in range(8):
        samekey=0; flag=True; i=1
        while(sameColor(x+dx[u]*i,y+dy[u]*i,key) or flag):
            if(not sameColor(x+dx[u]*i,y+dy[u]*i,key)):
                if(flag and inBoard(x+dx[u]*i,y+dy[u]*i) and num[x+dx[u]*i][y+dy[u]*i]!=0):
                    samekey-=10
                flag=False
            samekey+=1
            i+=1
        if(not downOk(x+dx[u]*i,y+dy[u]*i)):
            continue
        if(inBoard(x+dx[u]*(i-1),y+dy[u]*(i-1)) and num[x+dx[u]*(i-1)][y+dy[u]*(i-1)]==0):
            continue
        samekey,i=numofSamekey(x,y,u,1,key,samekey)
        if(not downOk(x+dx[u]*i,y+dy[u]*i)):
            continue
        if(samekey==3):
            s+=1
    return s
#该点在四个方向里，是否有六子或以上连线
def overLine(x,y):
    flag=False
    for u in range(4):
        if((numInline(x,y,u)+numInline(x,y,u+4))>4):
            flag=True
    return flag

#统计在u方向上，和key值相同的点的个数，即和key同色的连子个数
def numofSamekey(x,y,u,i,key,sk):
    if(i==1):
        while(sameColor(x+dx[u]*i,y+dy[u]*i,key)):
            sk+=1
            i+=1
    elif(i==-1):
        while(sameColor(x+dx[u]*i,y+dy[u]*i,key)):
            sk+=1
            i-=1
    return sk,i

#该黑子点是否是禁手点，黑子禁手直接判输
def ban(x,y):
    if(sameColor(x,y,3-go_first)):
        return False
    flag=((liveThree(x,y)>1) or (overLine(x,y)) or ((liveFour(x,y)+chongFour(x,y))>1))
    return flag

#游戏是否结束，如果有五子连线或出现禁手
def gameOver(x,y):
    global is_end
    for u in range(4):
        if((numInline(x,y,u)+numInline(x,y,u+4))>=4):
            is_end=True
            return True
    return False