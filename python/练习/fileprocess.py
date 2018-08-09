def save_file(boy,girl,count):
    file_name_boy='boy'+str(count)+'.txt'#文件的分别保存操作
    file_name_girl='girl'+str(count)+'.txt'
    boy_file=open(file_name_boy,'w')
    girl_file=open(file_name_girl,'w')
    boy_file.writelines(boy)
    girl_file.writelines(girl)
    boy_file.close()
    girl_file.close()
def split_file(filename):
    f=open(filename)
    boy =[]
    girl =[]
    count=1
    for eachline in f:
        if eachline [:6]!='======':
            (role,line_spoken)=eachline.split(':',1)#这里进行字符串分割操作
            if role == '小甲鱼':
                boy.append(line_spoken)
            if role == '小客服':
                girl.append(line_spoken)
        else:
            save_file(boy,girl,count)
            boy =[]
            girl =[]
            count+=1
    save_file(boy,girl,count)
    f.close()

split_file('record.txt')
