#171
from urllib.request import urlopen
url = 'https://www.python.org/'
with urlopen(url) as f:
    doc = f.read().decode()
    with open('phtyonhome.html','w') as h:
        h.writelines(doc)

###############################
#172 사이트가 사라져 실행안됨
from urllib.request import urlopen
imgurl = 'http://www.iaidol.com/img_sample.jpg'
imgname = imgurl.split('/')[-1]
try:
    with urlopen(imgurl) as f:
        with open(imgname,'wb') as h:
            img = f.read()
            h.write(img)
except Exception as e:
    print(e)

################################
#173
from urllib.request import urlopen
BUFSIZE = 256*1024
fileurl = 'https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe'
filename = fileurl.split('/')[-1]
try:
    with urlopen(fileurl) as f:
        with open(filename, 'wb') as h:
            buf = f.read(BUFSIZE)
            while buf:
                h.write(buf)
                buf = f.read(BUFSIZE)
except Exception as e:
    print(e)

###########################
#174
filename = 'python-3.8.2.exe'
subsize = 1024*1024*3
suffix = 0
with open(filename, 'rb') as f:
    buf = f.read(subsize)
    while buf:
        subfilename = filename + '_' + str(suffix)
        with open(subfilename, 'wb') as h:
            h.write(buf)
            print('[%s] 완료'%subfilename)
        buf = f.read(subsize)
        suffix += 1

###############################
#175 실행안됨
BUFSIZE = 256*1024
merge_filename = 'ret.exe'
filelist = ['python-3.8.2.exe_'+str(x) for x in range(10)]
with open(merge_filename, 'wb') as f:
    for filename in filelist:
        print('[%s] 합치는 중..'%filename)
        with open(filename, 'rb') as h:
            buf = h.read(BUFSIZE)
            while buf:
                f.write(buf)
                buf = h.read(BUFSIZE)
print('파일 합치기가 완료되었습니다.')

################################
#176
from zipfile import *
def compressZip(zipname, filename):
    print('[%s] -> [%s] 압축...'%(filename,zipname))
    with ZipFile(zipname, 'w') as ziph:
        ziph.write(filename)
    print('압축이 끝났습니다.')
filename = 'mydata.txt'
zipname = filename + '.zip'
compressZip(zipname, filename)

###########################
#177
from zipfile import *
import os
def compressAll(zipname, folder):
    print('[%s] -> [%s] 압축...'%(folder,zipname))
    with ZipFile(zipname, 'w') as ziph:
        for dirname, subdirs, files in os.walk(folder):
            for file in files:
                ziph.write(os.path.join(dirname, file))
folder = 'tmp'
zipname = folder + '.zip'
compressAll(zipname, folder)

###########################
#178실행안됨
from zipfile import *
def extractZip(zipname):
    with ZipFile(zipname, 'r') as ziph:
        ziph.extractall()
        print('[%s]가 성공적으로 추출되었습니다.'%zipname)
extractZip('file.zip')

####################################
#179
from random import shuffle
from time import sleep
gamenum = input('로또 게임 회수를 입력하세요 : ')
for i in range(int(gamenum)):
    balls = [x+1 for x in range(45)]
    ret = []
    for j in range(6):
        shuffle(balls)
        number = balls.pop()
        ret.append(number)
    ret.sort()
    print('로또번호[%d] : '%(i+1),end='')
    print(ret)
    sleep(1)

#############################
#180
from random import shuffle
male = ['슈퍼맨','심봉사','로미오','이몽룡','마루치']
female = ['원더우먼','뺑덕','줄리엣','성춘향','아라치']
shuffle(male)
shuffle(female)
couples = zip(male,female)
for i, couple in enumerate(couples):
    print('커플%d : [%s]-[%s]'%(i+1,couple[0],couple[1]))
























