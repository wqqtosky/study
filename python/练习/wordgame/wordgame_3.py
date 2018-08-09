#改进：当用户输入数据类型错误时，及时提醒用户，防止程序崩溃。

print("-----我爱鱼C工作室------")
print("猜我心里想的什么数：")
guess=0
n=3
while guess!=8 and n>0: #input的返回值始终是字符串，所以此处不能用type()和isinstance()函数
    temp=input()
    if temp.isdigit():
        guess=int(temp)
        if guess==8:
            print("猜对了")
            break
        else:
            if guess>8:
                print("哥，大了大了")
            else:
                print("哥，小了")
    else:
        print("输入不合法，请输入一个整数！")
    n=n-1
    if n>0:
        print("再给一次试验机会！")
    else:
        print("机会用完咯！")
print("游戏结束！")
