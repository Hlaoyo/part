from _2 import *


ai = 1 #AI下棋标志
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