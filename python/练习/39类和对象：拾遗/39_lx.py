class Turtle:
    def __init__(self,x):
        self.num = x
class Fish:
    def __init__(self,x):
        self.num = x
class Pool:
    def __init__(self,x,y):
        self.turtle = Turtle(x)   #直接把需要的类实例化，实例化出来一个乌龟
        self.fish = Fish(y)

    def print_num(self):
        print("水池里总共有乌龟 %d 只，小鱼 %d 条！" % (self.turtle.num,self.fish.num))

pool = Pool(1,10)
pool.print_num()
