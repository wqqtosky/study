#输入文件名以及开始搜索的路径，搜索该文件是否存在。如遇到文件夹，则进入继续搜索。
import os
def search_file(start_dir,target):
    os.chdir(start_dir)
    for each_file in os.listdir(os.curdir):
        if each_file == target :
            print(os.getcwd() + os.sep + each_file)
        if os.path.isdir(each_file):
            search_file(each_file,target) #递归调用
            os.chdir(os.pardir)           #递归调用后，一定要返回上一层目录

start_dir = input('请输入待查找的初始目录：')
target = input('请输入待查找的目标文件：')
search_file(start_dir,target)
