# スタッフスクロール
import time
from collections import deque

import CommandManager
import DrawDisplay

def run():
    staff_lines=list()

    # スタッフスクロールデータの読み込み
    with open("./data/staffScrollData.txt","r",encoding="utf-8") as f:
        staff_lines = f.readlines()

    # White spaceや改行を整形
    staff_lines=[line.strip("\n").replace("\u2003","  ") for line in staff_lines]

    screen_number=20 #一画面の長さ
    screen=deque(maxlen=screen_number)
    for _ in range(screen_number):
        screen.append("")#空行で埋める

    #表示部分
    for line in staff_lines:
        screen.append(line)
        DrawDisplay.initialDiplay(screen)
        time.sleep(0.5) #sleep
        DrawDisplay.clear()

    #最後にもう一度表示
    DrawDisplay.initialDiplay(screen)


if __name__=="__main__":
    run()
