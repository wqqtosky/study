#比较输入的俩个文件，显示出不同的行号
def file_compare(file1,file2):
    f1 =open(file1,'r')
    f2 =open(file2,'r')

    count =0
    differ=[] #统计不一样的行数量
    for line1 in f1:
        line2 = f2.readline()
        count+=1
        if line1 != line2:
            differ.append(count)
    f1.close()
    f2.close()
    return differ
file1=input('请输入要比较的第一个文件名')
file2=input('请输入要比较的第二个文件名')
differ = file_compare(file1,file2)
if len(differ)==0:
    print("两个文件完全一样")
else:
    print("两个文件有%d处不一样：" % len(differ))
    for each in differ:
        print("第 %d 行不一样" % each)
