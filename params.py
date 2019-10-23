from graphics import *
#import time

num = [[0 for a in range(16)] for a in range(16)]
dx = [1,1,0,-1,-1,-1,0,1] #x,y方向向量
dy = [0,1,1,1,0,-1,-1,-1]
is_end = False
go_first = 1 #先手标志
start = 1 #轮换下棋标志
#ai = 1 #AI下棋标志
L1_max=-100000 #剪枝阈值
L2_min=100000
list=[] #保存已画棋子
#RESTART_FLAG = False
#QUIT_FLAG = False
###
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
RESTART.setFill('red')