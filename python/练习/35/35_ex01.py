
import easygui as g
import random

g.msgbox("嗨，欢迎进入第一个界面小游戏")
secret = random.randint(1,10)
msg="猜我心里想的什么数(1-10)："
title="猜数字小游戏"
guess=g.integerbox(msg,title,lowerbound=1,upperbound=10)
while True: #input的返回值始终是字符串，所以此处不能用type()和isinstance()函数
    if guess==secret:
        g.msgbox("猜对了！！")
        g.msgbox("哼哼！")
        break
    else:
        if guess>secret:
            g.msgbox("哥，大了大了")
        else:
            g.msgbox("哥，小了")
        guess=g.integerbox(msg,title,lowerbound=1,upperbound=10)
g.msgbox("游戏结束！")
