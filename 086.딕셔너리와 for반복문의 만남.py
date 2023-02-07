store = {'새우칩':1500, '옥수수칩':1800,'콜라':700,'양파칩':1300}

for i,(key,value) in enumerate(store.items(),start=1):
    print('{} 번 물품은 {} 이고 가격은 {} 입니다'.format(i,key,value))
print(f'우리 가게는 모두 {len(store)} 개 종류의 물건이 있습니다')
print(f'우리 가게 물건들의 가격 총합은 {sum(store.values())} 입니다')

#enumerate에서 변수 갯수 맞추기 / 1부터 시작하려면 start=1
#딕셔너리의 등록된  item의 개수를 알려면 len(딕셔너리이름)을 활용
#sum(store.values()):value값 다더하기