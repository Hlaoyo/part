from params import *

def drawWin():
    win.setBackground('#cc8f33')
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
