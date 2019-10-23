# from graphics import *
# import time
# import sys
from part1 import *
# from part2 import *
# from part3 import *
from part5 import *
from part6 import *



"""
#num = [[0 for a in range(16)] for a in range(16)]
dx = [1,1,0,-1,-1,-1,0,1] #x,y方向向量
dy = [0,1,1,1,0,-1,-1,-1]
is_end = False
go_first = 1 #先手标志
start = 1 #轮换下棋标志
ai = 1 #AI下棋标志
L1_max=-100000 #剪枝阈值
L2_min=100000
list=[] #保存已画棋子
RESTART_FLAG = False
QUIT_FLAG = False"""

"""
###
##
win = GraphWin("五子棋",550,451)
aiFirst = Text(Point(500,100),"")
manFirst = Text(Point(500,140),"")
notice = Text(Point(500,290),"") #提示轮到谁落子
notice.setFill('red')
last_ai = Text(Point(500,330),"") #AI最后落子点
last_man = Text(Point(500,370),"") #玩家最后落子点
QUIT = Text(Point(500,20),"退出")
QUIT.setFill('red')
RESTART = Text(Point(500,60),"重玩")
RESTART.setFill('red')"""  #part1里面



#数据初始化，把棋盘上的棋子和提示清空
# def init():
#     global is_end,start,go_first,RESTART_FLAG
#     is_end=False
#     start=1
#     go_first=1
#     RESTART_FLAG=False
#     QUIT_FLAG=False
#     for i in range(16):
#         for j in range(16):
#             if(num[i][j]!=0):
#                 num[i][j]=0
#     for i in range(len(list)):
#         list[-1].undraw()
#         list.pop(-1)
#     aiFirst.setText("AI 先手")
#     manFirst.setText("我先手")
#     notice.setText("")
#     last_ai.setText("")
#     last_man.setText("")


#主程序入口
if __name__ == '__main__':
    init()
    drawWin()
    notice.setText("请选择先手")
    p=win.getMouse()
    while(not whoStart(p) and not Quit(p)):
        p=win.getMouse()
    while(not is_end):
        RESTART_FLAG=False
        if(start==ai):
            notice.setText("AI 正在下棋...")
            AI1()
        else:
            notice.setText("请你下棋...")
            manPlay()
        start=3-start
        if(RESTART_FLAG):
            notice.setText("请选择先手")
            p=win.getMouse()
            while(not whoStart(p) and not Quit(p)):
                p=win.getMouse()
        elif(not QUIT_FLAG and is_end):
            p=win.getMouse()
            while(not Restart(p) and not Quit(p)):
                p=win.getMouse()
            if(RESTART_FLAG):
                notice.setText("请选择先手")
                p=win.getMouse()
                while(not whoStart(p) and not Quit(p)):
                    p=win.getMouse()
