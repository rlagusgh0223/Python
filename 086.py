#86
txt1 = '안녕하세요?'
txt2 = '1. Title - 제목을 넣으세요'
txt3 = '3피오R2D2'
ret1 = txt1.isalnum()
ret2 = txt2.isalnum()
ret3 = txt3.isalnum()
print(ret1)
print(ret2)
print(ret3)

########################
#87
txt = 'A lot of Things occur each day.'
ret1 = txt.upper()
ret2 = txt.lower()
print(ret1)
print(ret2)

###########################
#88
txt = ' 양쪽에 공백이 있는 문자열입니다. '
ret1 = txt.lstrip()
ret2 = txt.rstrip()
ret3 = txt.strip()
print('<'+txt+'>')
print('<'+ret1+'>')
print('<' + ret2 + '>')
print('<' + ret3 + '>')

############################
#89
numstr = input('숫자를 입력하세요 : ')
try :
    num = int(numstr)
    print('당신이 입력한 숫자는 정수 <%d>입니다.'%num)
except :
    try :
        num = float(numstr)
        print('당신이 입력한 숫자는 실수<%f>입니다.'%num)
    except :
        print('+++숫자를 입력하세요~+++')

######################################
#90
num1 = 1234
num2 = 3.14
numstr1 = str(num1)
numstr2 = str(num2)
print('num1을 문자열로 변환한 값은 "%s"입니다.'%numstr1)
print('num2를 문자열로 변환한 값은 "%s"입니다.'%numstr2)























