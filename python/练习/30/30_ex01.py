# 编写一个程序，统计该文件夹下每个文件类型的文件数

import os
all_files=os.listdir('/media/wqq/新加卷/找工作书籍')
type_file=dict()   #创建一个空字典
os.chdir('/media/wqq/新加卷/找工作书籍')
for each_file in all_files:
    #each_file='/media/wqq/新加卷/找工作书籍/'+each_file #因为执行程序不是在文件得得当前路径下执行，所以需要用绝对路径
    #print(each_file)
    if os.path.isdir(each_file):        #判断文件是否是目录
        type_file.setdefault('文件夹',0) #字典中国没有这一项时自动添加，有的话则不会执行
        type_file['文件夹']+=1            #每一次让文件夹数量加1
    else:
        ext = os.path.splitext(each_file)[1] #splitext方法分离出文件名与扩展名，存在元组里，这里取出扩展名
        type_file.setdefault(ext,0)
        type_file[ext]+=1

for each_type in type_file.keys():
    print('该文件夹下共有类型为【%s】的文件%d个' % (each_type,type_file[each_type]))
