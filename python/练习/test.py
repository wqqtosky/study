#try:
# f = open('我为什么是一个文件.txt')
#  print(f.read())
#  f.close()
#except OSError as reason:
#  print('文件出错啦T_T\n错误的原因是：'+str(reason))


try:
    for i in range(3):
        for j in range(3):
            if(i==2):
                raise KeyboardInterrupt
            print(i,j)
except KeyboardInterrupt:
    print('退出啦！')
