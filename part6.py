
import time
from graphics import *
from params import *
# from themain import *

def init():
    global is_end,start,go_first,RESTART_FLAG
    is_end=False
    start=1
    go_first=1
    RESTART_FLAG=False
    QUIT_FLAG=False
    for i in range(16):
        for j in range(16):
            if(num[i][j]!=0):
                num[i][j]=0
    for i in range(len(list)):
        list[-1].undraw()
        list.pop(-1)
    aiFirst.setText("AI 先手")
    manFirst.setText("我先手")
    notice.setText("")
    last_ai.setText("")
    last_man.setText("")

# ##是否重新开始游戏
# def Restart(p):
#     global RESTART_FLAG
#     x = p.getX();
#     y = p.getY()
#     if ((abs(500 - x) < 40) and (abs(60 - y) < 15)):  # restart
#         init()
#         RESTART_FLAG = True
#         notice.setText("重新开始")
#         time.sleep(1)
#         return True
#     else:
#         return False
#
#
# ##是否退出游戏
# def Quit(p):
#     global QUIT_FLAG, is_end
#     x = p.getX();
#     y = p.getY()
#     if ((abs(500 - x) < 40) and (abs(20 - y) < 15)):  # quit
#         init()
#         QUIT_FLAG = True
#         is_end = True
#         notice.setText("退出")
#         time.sleep(1)
#         return True
#     else:
#         return False


##选择先后手
def whoStart(p):
    global start, go_first
    x = p.getX();
    y = p.getY()
    if ((abs(500 - x) < 40) and (abs(100 - y) < 15)):  # AI 先手
        start = 1
        go_first = 1
        aiFirst.setText("AI 执黑")
        manFirst.setText("玩家执白")
        return True
    elif ((abs(500 - x) < 40) and (abs(140 - y) < 15)):  # 玩家先手
        start = 2
        go_first = 2
        aiFirst.setText("AI 执白")
        manFirst.setText("玩家执黑")
        return True
    else:
        return False


