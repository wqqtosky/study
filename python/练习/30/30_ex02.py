# 编写一个程序，计算该文件夹下所有文件的大小

import os
all_files=os.listdir('/media/wqq/新加卷/找工作书籍')
size_file=dict()   #创建一个空字典
os.chdir('/media/wqq/新加卷/找工作书籍')
for each_file in all_files:

    #each_file='/media/wqq/新加卷/找工作书籍/'+each_file #因为执行程序不是在文件得得当前路径下执行，所以需要用绝对路径
    #print(each_file)
    if os.path.isfile(each_file):        #判断文件是否是文件类型
        filesize = os.path.getsize(each_file)
        size_file.setdefault(each_file,0)
        size_file[each_file] =filesize

for each_type in size_file.keys():
    print('%s 【%dBytes】' % (each_type,size_file[each_type]))
