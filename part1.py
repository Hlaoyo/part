from graphics import *
from params import *
# import time
#
# win = GraphWin("五子棋",550,451)
# aiFirst = Text(Point(500,100),"")
# manFirst = Text(Point(500,140),"")
# notice = Text(Point(500,290),"") #提示轮到谁落子
# notice.setFill('red')
# last_ai = Text(Point(500,330),"") #AI最后落子点
# last_man = Text(Point(500,370),"") #玩家最后落子点
# QUIT = Text(Point(500,20),"退出")
# QUIT.setFill('red')
# RESTART = Text(Point(500,60),"重玩")
# RESTART.setFill('red')

#画棋盘
def drawWin():
    win.setBackground('yellow')
    for i in range(0,451,30):
        line=Line(Point(i,0),Point(i,450))
        line.draw(win)
    for j in range(0,451,30):
        line=Line(Point(0,j),Point(450,j))
        line.draw(win)
    Rectangle(Point(460,5),Point(540,35)).draw(win)
    Rectangle(Point(460,45),Point(540,75)).draw(win)
    Rectangle(Point(460,85),Point(540,115)).draw(win)
    Rectangle(Point(460,125),Point(540,155)).draw(win)
    Rectangle(Point(452,275),Point(548,305)).draw(win)
    Rectangle(Point(452,307),Point(548,395)).draw(win)
    aiFirst.draw(win)
    manFirst.draw(win)
    notice.draw(win)
    last_ai.draw(win)
    last_man.draw(win)
    QUIT.draw(win)
    RESTART.draw(win)