
#改进：产生答案是随机的
#     限制输入次数
#     优先级：比较运算符>逻辑运算符
import random
#secret = random.randint(1,10)
secret = 5
print("-----我爱鱼C工作室------")
temp=input("猜我心里想的什么数：")
guess=int(temp)
i = 3
print(secret)
while guess!=secret and i>0:

    if guess>secret:
        print("哥，大了大了")
    else:
        print("哥，小了")
    temp=input("哎呀，出错了，请重新输入：")
    guess=int(temp)
    i = i-1
    print(i)
if guess==secret:
    print("猜对了")
else:
    print("答错了，猜测次数达到上限")
print("游戏结束！")
