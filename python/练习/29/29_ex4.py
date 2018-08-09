#当用户输入文件名和指定行范围，将该文件的指定行范围打印到屏幕上
def file_view(file_name,line_num):
    print("111:%s" % line_num)
    if line_num.strip()==':':
        begin='1'
        end='-1'
        print("222:%s" % line_num)
    (begin,end)=line_num.split(':')
    print("333:%s %s" % (begin,end))
    if begin ==' ':
        begin='1'
    if end ==' ':
        end='-1'
    print("444:%s %s" % (begin,end))
    if begin =='1' and end=='-1':
        prompt='的全文'
    elif begin =='1':
        prompt='从开始到%s' % end
    elif end =='-1':
        prompt='从%s开始到结束' % begin
    else:
        prompt='从%s行开始到%s行' % (begin,end)
    print("\n文件%s%s的内容如下：\n" % (file_name,prompt))
    begin =int(begin)-1
    end =int(end)
    lines =end - begin
    f = open(file_name)
    for i in range(begin):
        f.readline()
    if lines < 0:
        print(f.read()) #全文
    else:
        for j in range(lines):
            print(f.readline(),end='')
    f.close()

file_name = input(r'请输入要打开的文件：')
line_num = input(r'请输入需要显示该文件的行数【格式如 13:21 或 ：21 或 21： 】：')

file_view(file_name,line_num)
