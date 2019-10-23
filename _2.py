#from params import *
from _1 import *

#判断该点是否在棋盘范围内
def inBoard(x,y):
    if(x>=0 and x<=15 and y>=0 and y<=15): return True
    else: return False
#判断该点是否可落子，即是否在棋盘内且没有落子
def downOk(x,y):
    if(inBoard(x,y) and num[x][y]==0): return True
    else: return False
#该点值是否和i值相等，即该点棋子颜色和i相同
def sameColor(x,y,i):
    if(inBoard(x,y) and num[x][y]==i): return True
    else: return False
#在给定的方向v(v区分正负)上，和该点同色棋子的个数
def numInline(x,y,v):
    i=x+dx[v]; j=y+dy[v]
    s=0; ref=num[x][y]
    if(ref==0): return 0
    while(sameColor(i,j,ref)):
        s=s+1; i=i+dx[v]; j=j+dy[v]
    return s

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
