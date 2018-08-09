import easygui as g
import os

title="打开文件"
msg="wqq"
file_path=g.fileopenbox(msg,title,default='/文档/*.txt')#通过文件打开框得到文件的路径

with open(file_path) as f:
    title=os.path.basename(file_path)
    msg = "文件【%s】的内容如下：" % title
    #text = f.read()
    text = list(f)
    g.textbox(msg,title,text)
