"""#151
import os
pdir = os.getcwd();print(pdir)
os.chdir('..');print(os.getcwd())
os.chdir(pdir);print(os.getcwd())

######################
#152
import os
newfolder = input('새로 생성할 디렉터리 이름을 입력하세요 : ')
try:
    os.mkdir(newfolder)
    print('[%s] 디렉터리를 새로 생성했습니다.'%newfolder)
except Exception as e:
    print(e)

#######################
#153
import os
target_folder = 'tmp'
k = input('[%s] 디렉터리를 삭제하겠습니까? (y/n)'%target_folder)
if k=='y':
    try:
        os.rmdir(target_folder)
        print('[%s] 디렉터리를 삭제했습니다.'%target_folder)
    except Exception as e:
        print(e)
        
#############################
#154
import shutil, os
target_folder = 'tmp'
print('[%s] 하위 모든 디렉터리 및 파일들을 삭제합니다.'%target_folder)
for file in os.listdir(target_folder):
    print(file)
k = input('[%s]를 삭제하겠습니까?(y/n)'%target_folder)
if k=='y':
    try:
        shutil.rmtree(target_folder)
        print('[%s]의 모든 하위 디렉터리와 파일들을 삭제했습니다.'%target_folder)
    except Exception as e:
        print(e)

###############################
#155
import os
from os.path import exists
dir_name = input('새로 생성할 디렉터리 이름을 입력하세요 : ')
if not exists(dir_name):
    os.mkdir(dir_name)
    print('[%s] 디렉터리를 생성했습니다.'%dir_name)
else:
    print('[%s]은(는) 이미 존재합니다.'%dir_name)

#####################################
#156
import os
from os.path import exists, isdir, isfile
files = os.listdir()
for file in files:
    if isdir(file):
        print('DIR : %s'%file)
for file in files:
    if isfile(file):
        print('FILE : %s'%file)

##########################
#157
from time import localtime, strftime
logfile = 'test.log'
def writelog(logfile, log):
    time_stamp = strftime('%Y - %m - %d %X\t',localtime())
    log = time_stamp + log +'\n'
    with open(logfile, 'a') as f:
        f.writelines(log)
writelog(logfile, '첫 번째 로깅 문장입니다.')

##############################
#158
from time import localtime
t = localtime()
start_day = '%d-01-01' %t.tm_year
elapsed_day = t.tm_yday
print('오늘은 [%s]이후 [%d]일째 되는 날입니다.'%(start_day, elapsed_day))

##############################
#159
from time import localtime
weekdays = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
t = localtime()
today = '%d-%d-%d' %(t.tm_year, t.tm_mon, t.tm_mday)
week = weekdays[t.tm_wday]
print('[%s] 오늘은 [%s]입니다.'%(today, week))
"""
###############################
#160
from datetime import datetime
start = datetime.now()
print('1에서 백만까지 더합니다.')
ret = 0
for i in range(1000000):
    ret += i
print('1에서 백만까지 더한 결과 : %d'%ret)
end = datetime.now()
elapsed = end - start
print('총 계산 시간 : ', end='');print(elapsed)
elapsed_ms = int(elapsed.total_seconds()*1000)
print('총 계산 시간 : %dms' %elapsed_ms)





























