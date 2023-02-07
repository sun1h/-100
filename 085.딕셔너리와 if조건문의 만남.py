store = {'새우칩':1500, '옥수수칩':1800,'콜라':700,'양파칩':1300}
print('물품을 입력하면 가격을 알려드립니다')
while True:
    search=input('물품 이름은?')
    if search in store.keys():
        print(f'{search}의 가격은 {store[search]} 입니다')
    else:
        print(f'{search}는 등록되어 있지 않습니다')
        break

# if search in store: 해도 됨!