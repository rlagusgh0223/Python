"""#131
names = {'Marry':10999,'Sams':2111,'Aimy':9778,'Tom':20245,
         'Michale':27115,'Bob':5887,'Kelly':7855}
ret1 = sorted(names)
print(ret1)
def f1(x):
    return x[0]
def f2(x):
    return x[1]
ret2=sorted(names.items(),key=f1)
print(ret2)
ret3=sorted(names.items(),key=f2)
print(ret3)
ret4=sorted(names.items(),key=f2,reverse=True)
print(ret4)

#################################
#132
ch=input('문자를 1개 입력하세요 : ')
if len(ch) != 0:
    ch = ch[0]
    chv = ord(ch)
    print('문자 : %s \t코드값 : %d[%s]'%(ch,chv,hex(chv)))

#########################################
#133
val = input('문자 코드값을 입력하세요 : ')
val = int(val)
try :
    ch = chr(val)
    print('코드값 : %d[%s], 문자 : %s'%(val, hex(val),ch))
except ValueError:
    print('입력한 <%d>에 대한 문자가 존재하지 않습니다!'%val)

#########################################
#134
expr1 = '2+3'
expr2 = 'round(3.7)'
ret1 = eval(expr1)
ret2 = eval(expr2)
print('<%s>를 eval()로 실행한 결과  :'%expr1,end='');print(ret1)
print('<%s>를 eval()로 실행한 결과 : '%expr2,end='');print(ret2)

#########################################
#135
add = lambda x,y : x+y
ret = add(1,3)
print(ret)
funcs = [lambda x : x+'.pptx', lambda x : x+'.docx']
ret1 = funcs[0]('intro')
ret2 = funcs[1]('Report')
print(ret1)
print(ret2)
names = {'Marry':10999,'Sams':2111,'Aimy':9778,'Tom':20245,
         'Michale':27115,'Bob':5887,'Kelly':7855}
ret3 = sorted(names.items(),key=lambda x:x[0])
print(ret3)

###########################################
#136
f = lambda x : x*x
args = [1,2,3,4,5]
ret = map(f, args)
print(list(ret))

#추가문제
f = lambda x,y : x*x+y
X = [1,2,3,4,5]
Y = [10,9,8,7,6]
ret = map(f,X,Y)
print(list(ret))

###################
#137
f = open('stockcode.txt','r')
data = f.read()
print(data)
f.close()

###################
#138
f = open('stockcode.txt','r')
line_num = 1
line = f.readline()
while line:
    print('%d %s' %(line_num,line),end='')
    line = f.readline()
    line_num += 1
f.close()

############################
#139
f = open('stockcode.txt','r')
lines = f.readlines()
for line_num, line in enumerate(lines):
    print('%d %s' %(line_num+1, line), end='')
f.close
"""
###############################
#140
text = input('파일에 저장할 내용을 입력하세요 : ')
f = open('mydata.txt','w')
f.write(text)
f.close()





















    
