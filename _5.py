#from params import *
from _4 import *

#选手下棋
def manPlay():
    p=win.getMouse()
    if(Restart(p) or Quit(p)): return
    x=round(p.getX()/30)
    y=round(p.getY()/30)
    if(downOk(x,y)): go(x,y)
    else: manPlay()

##是否重新开始游戏
def Restart(p):
    global RESTART_FLAG
    x=p.getX(); y=p.getY()
    if((abs(500-x)<40) and (abs(60-y)<15)): #restart
        init()
        RESTART_FLAG=True
        notice.setText("重新开始")
        time.sleep(1)
        return True
    else:
        return False
##是否退出游戏
def Quit(p):
    global QUIT_FLAG, is_end
    x=p.getX(); y=p.getY()
    if((abs(500-x)<40) and (abs(20-y)<15)): #quit
        init()
        QUIT_FLAG=True
        is_end=True
        notice.setText("退出")
        time.sleep(1)
        return True
    else:
        return False
##选择先后手
def whoStart(p):
    global start, go_first
    x=p.getX(); y=p.getY()
    if((abs(500-x)<40) and (abs(100-y)<15)): #AI 先手
        start=1
        go_first=1
        aiFirst.setText("AI 执黑")
        manFirst.setText("玩家执白")
        return True
    elif((abs(500-x)<40) and (abs(140-y)<15)): #玩家先手
        start=2
        go_first=2
        aiFirst.setText("AI 执白")
        manFirst.setText("玩家执黑")
        return True
    else:
        return False