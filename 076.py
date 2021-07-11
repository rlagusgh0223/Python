#76
txt1 = 'A tale that was not right'
txt2 = '이 또한 지나가리라.'
print(txt1[3:7])
print(txt1[:6])
print(txt2[-4:])
txt = 'python'
for i in range(len(txt)):
    print(txt[:i+1])
print('=================================')
#######################
#77
txt = 'aAbBcCdDeEfFgGhHiIjJkK'
ret = txt[::2]
print(ret)
ret = txt[1::2]
print(ret)
print('=================================')
#######################
#78
txt = 'abcdefghijk'
ret = txt[::-1]
print(ret)
ret = txt[::-2]
print(ret)
ret = txt[-2::-2]
print(ret)
print('=================================')
#######################
#79
filename = input('저장할 파일이름을 입력하세요:')
filename = filename + '.jpg'
display_msg = '당신이 저장한 파일은<' + filename + '>입니다.'
print(display_msg)
print('=================================')
#############################################
#80
msg1 = '여러분'
msg2 = '파이팅!'
display_msg = msg1 + ', ' + msg2*3 + '~!'
print(display_msg)












