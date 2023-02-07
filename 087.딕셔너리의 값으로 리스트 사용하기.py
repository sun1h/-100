store = {'새우칩':[1500,3], '옥수수칩':[1800,2],'콜라':[700,4],'양파칩':[1300,1]}


for i,(key,value) in enumerate(store.items(),start=1):
    print('{} 번 물품은 {} 이고 가격은 {} 이고 수량은 {} 개입니다'.format(i,key,value[0],value[1]))
print(f'우리 가게는 {len(store)} 개의 물건 종류가 있습니다')


li1=[]
li2=[]
for value in enumerate(store.values()):
    li1.append(value[1][1])
    li2.append(value[1][0])
total1=sum(li1)
total2=0
for i in range(len(li2)):
    total2+=li1[i]*li2[i]

print(f'우리 가게 모든 물건 수량은 {total1} 개 있습니다')
print(f'우리 가게 모든 물건들의 가격 총합은 {total2} 입니다')
print(f'우리 가게 모든 물건들의 평균 가격은 {total2/total1} 원입니다')
