#用户输入关键字，查找当前文件夹内（包含子文件夹）内所有所有含有该关键字的文本文件（.txt后缀）,要求显示该文件所在的位置以及关键字在文件中的具体位置（第几行第几个字符）。
import os

def print_pos(key_dict):
    keys = key_dict.keys()
    keys = sorted(keys) # 字典是无序的，这里对行数进行排序
    for each_key in keys:
        print('关键字出现在第 %s 行，第 %s 个位置。' % (each_key,str(key_dict[each_key])))
def pos_in_line(each_line,key):
    pos =[]
    begin = each_line.find(key)
    while begin != -1:
        pos.append(begin + 1)
        begin = each_line.find(key,begin + 1) #从下一个位置继续查找
    return pos

def search_in_txtfile(file_name,key):
    f = open(file_name)
    count =0
    key_dict =dict()


    for each_line in f:
        count+=1
        if key in each_line:#若关键字存在于这行，则继续查找关键字在这行的具体位置
            pos = pos_in_line(each_line,key) # key在每行的位置，存在列表中
            key_dict[count] = pos
    f.close()
    return key_dict

def search_files(key,detail):
    all_files = os.walk(os.getcwd())
    txt_files =[]
    #print(all_files)
    for i in all_files:        #找出文件夹及其子文件夹中的.txt文件，并存放
        for each_file in i[2]:
            #print(each_file)
            if os.path.splitext(each_file)[1] == '.txt':#获取文件的后缀
                each_file = os.path.join(i[0],each_file)#给文件加上路径
                txt_files.append(each_file)
    print(txt_files)
    for each_text_file in txt_files: #在.txt文件中查找关键字，并把查找结果保存在key_dict中
        key_dict = search_in_txtfile(each_text_file,key)
        if key_dict:  #字典不为空，则说明在该文件中找到关键字
            print('==================================================')
            print('在文件【%s】中找到关键字【%s】'% (each_text_file,key))
            if detail in ['YES','Yes','yes']:
                print_pos(key_dict)


key = input('请将该脚本放于待查找的文件夹内，请输入关键字：')
detail = input('请问是否需要打印关键字【%s】在文件中的具体位置（YES/NO）:' % key)

search_files(key,detail)
