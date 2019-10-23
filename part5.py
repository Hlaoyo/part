# from themain import *
from part2 import *
from part6 import *
from part3 import *
import graphics
from params import *

# dx = [1,1,0,-1,-1,-1,0,1] #x,y方向向量
# dy = [0,1,1,1,0,-1,-1,-1]
# is_end = False
# #go_first = 1 #先手标志
# start = 1 #轮换下棋标志
ai = 1 #AI下棋标志
# L1_max=-100000 #剪枝阈值
# L2_min=100000
# list=[] #保存已画棋子
# RESTART_FLAG = False
# QUIT_FLAG = False

##是否重新开始游戏
def Restart(p):
    global RESTART_FLAG
    x = p.getX();
    y = p.getY()
    if ((abs(500 - x) < 40) and (abs(60 - y) < 15)):  # restart
        init()
        RESTART_FLAG = True
        notice.setText("重新开始")
        time.sleep(1)
        return True
    else:
        return False


##是否退出游戏
def Quit(p):
    global QUIT_FLAG, is_end
    x = p.getX();
    y = p.getY()
    if ((abs(500 - x) < 40) and (abs(20 - y) < 15)):  # quit
        init()
        QUIT_FLAG = True
        is_end = True
        notice.setText("退出")
        time.sleep(1)
        return True
    else:
        return False
#落下一子并且判断游戏是否结束
def go(x,y):
    global is_end
    c=Circle(Point(x*30,y*30),13)
    if(start==ai):
        num[x][y]=ai
        last_ai.setText("AI 落子:\n(x:y)=("+str(x)+":"+str(y)+")")
        if(go_first==ai): c.setFill('black')
        else: c.setFill('white')
    else:
        num[x][y]=3-ai
        last_man.setText("玩家落子:\n(x:y)=("+str(x)+":"+str(y)+")")
        if(go_first==ai): c.setFill('white')
        else: c.setFill('black')
    c.draw(win)
    list.append(c)
    if(ban(x,y)):
        if(start==ai):
            notice.setText("AI 禁手,玩家赢!\n点击重玩")
        else:
            notice.setText("玩家禁手,AI 赢!\n点击重玩")
        is_end=True
    elif(gameOver(x,y)):
        if(start==ai):
            notice.setText("AI 赢!\n点击重玩")
        else:
            notice.setText("玩家赢!\n点击重玩")

#该黑子点是否是禁手点，黑子禁手直接判输
def ban(x,y):
    if(sameColor(x,y,3-go_first)):
        return False
    flag=((liveThree(x,y)>1) or (overLine(x,y)) or ((liveFour(x,y)+chongFour(x,y))>1))
    return flag


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
#选手下棋
def manPlay():
    p=win.getMouse()
    if(Restart(p) or Quit(p)): return
    x=round(p.getX()/30)
    y=round(p.getY()/30)
    if(downOk(x,y)): go(x,y)
    else: manPlay()

