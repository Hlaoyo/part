from _5 import *
import time

QUIT_FLAG = False
#主程序入口
if __name__=='__main__':
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