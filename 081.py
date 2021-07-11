#81
msg = input('임의의 문장을 입력하세요 : ')
if 'a' in msg :
    print('당신이 입력한 문장에는 a가 있습니다.')
else :
    print('당신이 입력한 문장에는 a가 없습니다.')

###############################
#82
msg = input('임의의 문장을 입력하세요 : ')
if 'is' in msg :
    print('당신이 입력한 문장에는 is가 있습니다.')
else :
    print('당신이 입력한 문장에는 is가 없습니다.')

###############################
#83
msg = input('임의의 문장을 입력하세요 : ')
#msglen = len(msg)
msglen = len(msg.encode())
print('당신이 입력한 문장의 길이는 <%d>입니다.'%msglen)

######################################
#84
txt1 = 'A'
txt2 = '안녕'
txt3 = 'Warcraft Three'
txt4 = '3PO'
ret1 = txt1.isalpha()
ret2 = txt2.isalpha()
ret3 = txt3.isalpha()
ret4 = txt4.isalpha()
print(ret1)
print(ret2)
print(ret3)
print(ret4)

#######################################
#85
txt1 = '010-1234-5678'
txt2 = 'R2D2'
txt3 = '1212'
ret1 = txt1.isdigit()
ret2 = txt2.isdigit()
ret3 = txt3.isdigit()
print(ret1)
print(ret2)
print(ret3)








