#96
u_txt = 'I love python'
b_txt = u_txt.encode()
print(u_txt)
print(b_txt)

ret1 = 'I' == u_txt[0]
ret2 = 'I' == b_txt[0]
print(ret1)
print(ret2)

#####################
#97
b_txt = b'A lot of things occur each day.'
u_txt = b_txt.decode()
print(u_txt)

###############################
#98
strdata = input('정렬할 문자열을 입력하세요 : ')
ret1 = sorted(strdata)
ret2 = sorted(strdata, reverse=True)
print(ret1)
print(ret2)
ret1 = ''.join(ret1)
ret2 = ''.join(ret2)
print('오름차순으로 정렬된 문자열은 <'+ret1+'>입니다.')
print('내림차순으로 정렬된 문자열은 <'+ret2+'>입니다.')
#추가문제
strdata = 'wqertyuiop34195'
ret1 = ''.join(sorted(strdata))
ret2 = ''.join(sorted(strdata,reverse=True))
print(ret1)
print(ret2)

###################################
#99
range1 = range(10)
range2 = range(10,20)
print(list(range1))
print(list(range2))
ret=0
for i in range(10):
    ret += (i+1)
    print(ret)

####################
#100
listdata = [1,2,'a','b','c',[4,5,6]]
val1 = listdata[1]
val2 = listdata[3]
val3 = listdata[5][1]
val4 = listdata[5]
print(val1)
print(val2)
print(val3)
print(val4)













