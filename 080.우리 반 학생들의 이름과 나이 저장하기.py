dic=dict(메이킷=17,우진=9,시은=11,제임스=10) #문자열 처리 하지 않고 바로 할당
print(dic)

#다른방법
store = {'새우칩':1000, '옥수수칩':1200} 

#zip함수사용
lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72])) 

#튜플로 나열하는 법
lux3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])