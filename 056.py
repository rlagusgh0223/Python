try:
    print('안녕하세요')
#    print(param)
except:
    print('예외가 발생했습니다.')
else:
    print('예외가 발생하지 않았습니다.')
########################
try:
    print('안녕하세요')
#    print(param)
except:
    print('예외가 발생했습니다.')
finally:
    print('무조건 실행하는 코드')
#######################
try:
    print(param)
except Exception as i:
    print(i)
#########################
import time
count=1
try:
    while True:
        print(count)
        count+=1
        time.sleep(0.5)
except KeyboardInterrupt:
    print('사용자에 의해 프로그램이 중단되었습니다.')
###########################
k=input('<값>을 입력하세요')
print('당신이 입력한 값은 <'+k+'>입니다.')
