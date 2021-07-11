numdata = 57
strdata = '파이썬'
listdata = [1,2,3]
dictdata = {'a':1, 'b':2}
def func():
    print('안녕하세요')
print(type(numdata))
print(type(strdata))
print(type(listdata))
print(type(dictdata))
print(type(func))
########################
a=11113
b=23
ret=a%b
print('<%d>를 <%d>로 나누면 <%d>가 나머지로 남습니다.'%(a,b,ret))
##################
a=11113
b=23
ret1,ret2=divmod(a,b)
print('<%d>/<%d>는 몫이 <%d>, 나머지가 <%d>입니다.'%(a,b,ret1,ret2))
######################
h1=hex(97)
h2=hex(98)
ret1=h1+h2
print(ret1)
a=int(h1,16)
b=int(h2,16)
ret2=a+b
print(hex(ret2))
###################
n=159
print('%X'%n)
print('%x'%n)
#############
n=11
print('%02X'%n)
print('%02x'%n)
################
b1=bin(97)
b2=bin(98)
ret1=b1+b2
print(ret1)
a=int(b1,2)
b=int(b2,2)
ret2=a+b
print(bin(ret2))






















