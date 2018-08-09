filename =input("请输入文件名:")
f =open(filename,'w')
print("请输入内容【单独输入：w保存退出】")

string =input()
data=[]
while (string !=':w'):
    data.append(string+'\n')
    string =input()
f.writelines(data)
f.close()



def file_write(file_name):
    f =open(file_name,'w')
    print("请输入内容【单独输入：w保存退出】")
    while True:
        string =input()
        if string !=':w':
            f.write('%s\n' % string)
        else:
            break
    f.close()
file_name =input("请输入文件名:")
file_write(file_name)
