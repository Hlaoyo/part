from params import *
# num = [[0 for a in range(16)] for a in range(16)]

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