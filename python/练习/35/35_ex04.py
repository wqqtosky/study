import easygui as g
import os

title="打开文件"
msg="wqq"
file_path=g.fileopenbox(msg,title,default='/home/wqq/文档/')#通过文件打开框得到文件的路径

with open(file_path) as f:
    title=os.path.basename(file_path)#去掉目录路径，单独返回文件名
    msg = "文件【%s】的内容如下：" % title
    text_before = f.read() #将读取内容以字符串形式
    #text_before = list(f) #将读取内容放进列表
    print(text_before)
    text_after=g.textbox(msg,title,text_before)
    print(text_after[:-1])

 #textbox()在返回的字符串后面都加上一个行结束符（”\n“），因此在比较字符串时需要将这个行结束符去掉
if text_before != text_after[:-1]:
    choice = g.buttonbox("检测到文件内容发生改变，请选择以下操作：","警告",("覆盖保存","放弃保存","另存为..."))
    if choice == "覆盖保存":
        with open(file_path,'w') as f:
            f.write(text_after[:-1])
    if choice == "放弃保存":
        pass
    if choice == "另存为...":
        another_path = g.filesavebox("wqq",default="wqq",filetypes = ["*.txt"])
        if os.path.splitext(another_path)[1] != '.txt':#分离文件名和扩展名，返回二元元组
            another_path+='.txt'
        with open(another_path,'w') as new_file:
            new_file.write(text_after[:-1])
