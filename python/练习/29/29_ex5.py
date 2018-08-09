#将指定文件内的指定字符串进行全部替换
def file_replace(file_name,old_word,new_word):
    f = open(file_name)
    content = []  #存放更改后的内容
    count = 0     #记录原字符的个数
    for eachline in f:
        if old_word in eachline:
            count += eachline.count(old_word)
            eachline = eachline.replace(old_word,new_word)
        content.append(eachline)
    #print(content)
    decide = input('\n文件 %s 中共有%s个【%s】\n您确定要把所有的【%s】替换为【%s】吗？\n【yes/no】: ' % (file_name,count,old_word,old_word,new_word))
    if decide in ['YES','Yes','yes']:
        f_write = open(file_name,'w')
        f_write.writelines(content)
        f_write.close()
    f.close()
file_name = input(r'请输入要打开的文件：')
old_word= input(r'请输入需要替换的单词或字符：')
new_word= input(r'请输入新的单词或字符：')
file_replace(file_name,old_word,new_word)
