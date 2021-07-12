#101
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성','지구']
planet = '지구'
pos = solarsys.index(planet)
print('%s은(는) 태양계에서 %d번째 위치하고 있습니다.'%(planet,pos))
pos = solarsys.index(planet, 5)
print('%s은(는) 태양계에서 %d번째 위치하고 있습니다.'%(planet,pos))

##############################################
#102
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
planet = '화성'
pos = solarsys.index(planet)
solarsys[pos] = 'Mars'
print(solarsys)

##############################################
#103
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
rock_planets = solarsys[1:4]
gas_planets = solarsys[4:]
print('태양계의 암석형 행성 : ',end='');print(rock_planets)
print('태양계의 가스형 행성 : ',end='');print(gas_planets)

##############################################
#104
listdata = list(range(1,21))
evenlist = listdata[1::2]
print(evenlist)
oddlist = listdata[::2]
print(oddlist)

#################
#105
listdata = list(range(5))
listdata.reverse()
print(listdata)\

#################
#106
listdata = list(range(5))
ret1 = reversed(listdata)
print('원본 리스트', end='');print(listdata)
print('역순 리스트',end='');print(list(ret1))
ret2 = listdata[::-1]
print('슬라이싱 이용 ',end='');print(ret2)

############################
#107
listdata1 = ['a','b','c','d','e']
listdata2 = ['f','g','h','i','j']
listdata3 = listdata1 + listdata2
listdata4 = listdata2 + listdata1
print(listdata3)
print(listdata4)

#######################
#108
listdata = list(range(3))
ret = listdata*3
print(ret)

#######################
#109
listdata = []
for i in range(3):
    txt = input('리스트에 추가할 값을 입력하세요[%d/3] : '%(i+1))
    listdata.append(txt)
    print(listdata)

#######################
#110
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
pos = solarsys.index('목성')
solarsys.insert(pos, '소행성')
print(solarsys)


























