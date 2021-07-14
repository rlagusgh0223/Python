#121
listdata = [2,2,1,3,8,5,7,6,3,6,2,3,9,4,4]
ret = sum(listdata)
print(ret)

###########################
#122
listdata1 = [0,1,2,3,4]
listdata2 = [True, True, True]
listdata3 = ['',[],(),{},None,False]
print(all(listdata1))
print(any(listdata1))
print(all(listdata2))
print(any(listdata2))
print(all(listdata3))
print(any(listdata3))

###########################
#123
solar1=['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
solar2=['Sun','Mercury','Venus','Earth','Mars','Jupiter','Satrun','Uranus','Neptune']
solardict={}
for i,k in enumerate(solar1):
    val = solar2[i]
    solardict[k] = val
print(solardict)

#####################
#124
names = {'Marry':10999,'Sams':2111,'Aimy':9778,'Tom':20245,'Michale':27115,'Bob':5887,'Kelly':7855}
names['Aimy'] = 10000
print(names)

#####################
#125
names = {'Marry':10999,'Sams':2111,'Aimy':9778,'Tom':20245,
         'Michale':27115,'Bob':5887,'Kelly':7855}
del names['Sams']
print(names)

#####################
#126
names = {'Marry':10999,'Sams':2111,'Aimy':9778,'Tom':20245,
         'Michale':27115,'Bob':5887,'Kelly':7855}
names.clear()
print(names)

###########
#127
names = {'Marry':10999,'Sams':2111,'Aimy':9778,'Tom':20245,
         'Michale':27115,'Bob':5887,'Kelly':7855}
ks = names.keys()
print(ks)
for k in ks:
    print('Key : %s \t Value : %d'%(k,names[k]))

################################
#128
names = {'Marry':10999,'Sams':2111,'Aimy':9778,'Tom':20245,
         'Michale':27115,'Bob':5887,'Kelly':7855}
vals = names.values()
print(vals)
vals_list = list(vals)
ret = sum(vals_list)
print('출생아 수 총계 : %d'%ret)

############################
#129
names = {'Marry':10999,'Sams':2111,'Aimy':9778,'Tom':20245,
         'Michale':27115,'Bob':5887,'Kelly':7855}
items = names.items()
print(items)
for item in items:
    print(item)

#############################
#130
names = {'Marry':10999,'Sams':2111,'Aimy':9778,'Tom':20245,
         'Michale':27115,'Bob':5887,'Kelly':7855}
k = input('이름을 입력하세요 : ')
if k in names:
    print('이름이 <%s>인 출생아 수는 <%d>명입니다.'%(k,names[k]))
else:
    print('자료에 %<%s>인 이름이 존재하지 않습니다.'%k)

if 2111 in names.values():
    print('주어진 값이 사전에 존재합니다.')
else:
    print('주어진 값이 사전에 존재하지 않습니다.')























