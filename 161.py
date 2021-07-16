#161
num = input('아무 숫자를 입력하세요 : ')
if num.isdigit():
    num = num[::-1]
    ret=''
    for i,c in enumerate(num):
        i += 1
        if i!= len(num) and i%3 == 0:
            ret += (c+',')
        else:
            ret +=c
    ret = ret[::-1]
    print(ret)
else:
    print('입력한 내용[%s]: 숫자가 아닙니다.'%num)

#################################
#162
text = input('문장을 입력하세요 : ')
ret = ''
for i in range(len(text)):
    if i != len(text) -1:
        ret += text[i+1]
    else:
        ret += text[0]
print(ret)

#########################
#163
url = 'https://book.naver.com/search/search.nhn?query=%EC%BA%90%EA%B8%80'
tmp = url.split('/')
domain = tmp[2]
print(domain)

#########################
#164
url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%BA%90%EA%B8%80'
tmp = url.split('?')
queries = tmp[1].split('&')
for query in queries:
    print(query)

######################
#165
mystack = []
def putdata(data):
    global mystack
    mystack.append(data)
def popdata():
    global mystack
    if len(mystack) == 0:
        return None
    return mystack.pop()
putdata('데이터1')
putdata([3,4,5,6])
putdata(12345)
print('<스택상태> : ',end='');print(mystack)
ret = popdata()
while ret != None:
    print('스택에서 데이터 추출 : ',end='');print(ret)
    print('<스택상태> : ',end='');print(mystack)
    ret = popdata()

###################################
#166
def getTextFreq(filename):
    with open(filename,'r') as f:
        text = f.read()
        fa = {}
        for c in text:
            if c in fa:
                fa[c] += 1
            else:
                fa[c] = 1
        return fa
ret = getTextFreq('mydata.txt')
ret = sorted(ret.items(), key=lambda x:x[1],reverse=True)
for c, freq in ret:
    if c == '\n':
        continue
    print('[%c] -> [%d]회 나타남'%(c,freq))

###############################
#167
with open('mydata.txt','r') as f:
    data = f.read()
    tmp = data.split()
    print('단어수 : [%d]'%len(tmp))

##############################
#168
def countWord(filename, word):
    with open(filename, 'r') as f:
        text = f.read()
        text = text.lower()
        pos = text.find(word)
        count = 0
        while pos != -1:
            count += 1
            pos = text.find(word, pos+1)
    return count
word = input('mydata.txt에서 개수를 구할 단어를 입력하세요 : ')
word = word.lower()
ret = countWord('mydata.txt', word)
print('[%s[의 개수 : %d'%(word, ret))

#################################
#169
t1 = input('찾을 단어를 입력하세요 : ')
t2 = input('변경할 단어를 입력하세요 : ')
with open('mydata.txt','r') as f:
    with open('mydata2.txt','w') as h:
        text = f.read()
        text = text.replace(t1,t2)
        h.write(text)
print('[%s]를 [%s]로 변경하였습니다'%(t1,t2))

##################################
#170
from urllib.request import urlopen
url = 'https://www.python.org'
with urlopen(url) as f:
    doc = f.read().decode()
    print(doc)
