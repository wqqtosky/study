# 在linux系统上安装easygui:
## 步骤：
1、在小甲鱼官方网站上下载：带文档的压缩包，http://bbs.fishc.com/thread-48047-1-1.html
2、教学文档有小甲鱼翻译的版本，http://bbs.fishc.com/thread-46069-1-1.html
3、开始安装：切换到命令行模式
- 在命令窗口切换到easygui-docs-0.96的目录下
- 【windows】:C:\python3\python.exe setup.py install
- 【linux】: sudo setup.py install
**注：在linux下，因为有两个版本的python,默认会装进python2版本里，所以对于python3还需要再做处理,操作如下：**
1、把easygui文件夹转移至python3.5的包文件夹`/usr/local/lib/python3.5/dist-packages`。(mv)
2、由于tkinter包会存在不兼容的问题，所以需要对他进行更新，输入命令:`sudo apt-get install python3-tk`
3、这时候，在python3.5的模式下输入`import easygui`，就不会出错了。
`
