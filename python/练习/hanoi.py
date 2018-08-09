def hanoi(n,x,y,z):
    if n==1:
        print(x,'-->',z)
    else:
        hanoi(n-1,x,z,y)
        print(x,'-->',z)
        hanoi(n-1,y,x,z)

n = int(input("请输入汉诺塔的层数："))
hanoi(n,'x','y','z')
#将前n-1个盘子从y移动到z
#将前n-1个盘子从x移动到y
