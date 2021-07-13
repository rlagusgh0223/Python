#111
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
del solarsys[0]
print(solarsys)
del solarsys[-2]
print(solarsys)

##############
#112
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
solarsys.remove('태양')
print(solarsys)

################
#113
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
del solarsys[1:3]
print(solarsys)

################
#114
listdata = [2,2,1,3,8,5,7,6,3,6,2,3,9,4,4]
listsize = len(listdata)
print(listsize)

#############################
#115
listdata = [2,2,1,3,8,5,7,6,3,6,2,3,9,4,4]
c1 = listdata.count(2)
c2 = listdata.count(7)
print(c1)
print(c2)

#############################
#116
listdata = [2,2,1,3,8,5,7,6,3,6,2,3,9,4,4]
del listdata
print(listdata)

#############################
#117
namelist = ['Marry','Sams','Aimy','Tom','Michale','Bob','Kelly']
#namelist.sort()
namelist.sort(reverse=True)
print(namelist)

#############################
#118
namelist = ['Marry','Sams','Aimy','Tom','Michale','Bob','Kelly']
ret1 = sorted(namelist)
ret2 = sorted(namelist,reverse=True)
print(namelist)
print(ret1)
print(ret2)

###########################
#119
from random import shuffle
listdata = list(range(1,11))
for i in range(3):
    shuffle(listdata)
    print(listdata)

####################
#120
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
ret = list(enumerate(solarsys))
print(ret)
for i, body in enumerate(solarsys):
    print('태양계의 %d번째 천체 : %s'%(i,body))


























