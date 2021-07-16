"""#141
count = 1
data = []
print('파일에 내용을 저장하려면 내용을 입력하지 말고 [Enter]를 누르세요')
while True:
    text = input('[%d]파일에 저장할 내용을 입력하세요 : '%count)
    if text =='':
        break
    data.append(text+'\n')
    count += 1
f = open('mydata.txt','w')
f.writelines(data)
f.close()

###########################
#142
f = open('stockcode.txt','r')
h = open('stockcode_copy.txt','w')
data = f.read()
h.write(data)
f.close()
h.close()

#################
#143
bufsize = 1024
f = open('img_sample.jpg','rb')
h = open('img_sample_copy.jpg','wb')
data = f.read(bufsize)
while data:
    h.write(data)
    data = f.read(bufsize)
f.close()
h.close()

###################
#144
with open('stockcode.txt','r') as f:
    for line_num, line in enumerate(f.readlines()):
        print('%d %s'%(line_num+1, line),end='')

###############################
#145
spos = 105
size = 500
f = open('stockcode.txt','r')
h = open('stockcode_part.txt','w')
f.seek(spos)
data = f.read(size)
h.write(data)
h.close()
f.close()

#############################
#146
from os.path import getsize
file1 = 'stockcode.txt'
file2 = 'img_sample.jpg'
file_size1 = getsize(file1)
file_size2 = getsize(file2)
print('File Name : %s\tFile Size : %d'%(file1,file_size1))
print('File Name : %s\tFile Size : %d'%(file2,file_size2))

########################################
#147
from os import remove
target_file = 'stockcode_copy.txt'
k = input('[%s]파일을 삭제하겠습니까?(y/n)'%target_file)
if k=='y':
    remove(target_file)
    print('[%s]를 삭제했습니다.'%target_file)
elif k=='n':
    print('[%s]를 삭제하지 않았습니다.'%target_file)

#########################################
#148
from os import rename
target_file = 'stockcode.txt'
newname = input('[%s]에 대한 새로운 파일이름을 입력하세요 : '%target_file)
rename(target_file,newname)
print('[%s] -> [%s]로 파일이름이 변경되었습니다.'%(target_file,newname))

##################################
#149
from os import rename
target_file = 'stockcode.txt'
newpath = input('[%s]를 이동할 디렉터리의 절대경로를 입력하세요 : '%target_file)
if newpath[-1] == '/':
    newname = newpath + target_file
else:
    newname = newpath +'/' + target_file
try:
    rename(target_file, newname)
    print('[%s] -> [%s]로 이동되었습니다.'%(target_file, newname))
except FileNotFoundError as e:
    print(e)
"""
##############################
#150
import os, glob
folder = 'C:\Users\Owner\Desktop\khh\git\python'
file_list = os.listdir(folder)
print(file_list)

files='*.txt'
file_list = glob.glob(files)
print(file_list)



























