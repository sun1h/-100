test={'우진이':{'코딩':95, '수학':99},'시은이':{'과학':100,'코딩':99},'메이킷':{'영어':85,'코딩':100}}

# print(f"우진이의 코딩 점수는?{test['우진']['코딩']}")
# print(f"시은이의 과학 점수는?{test['시은']['과학']}")
# print(f"메이킷의 영어 점수는?{test['메이킷']['영어']}")

#더나아가서 value2, value3을 순회적으로 출력하는 법
for key1,(key2,key3) in test.items():
    print(f'{key1}의 {key2} 점수는?{test[key1][key2]}')
    #print(key1,test[key1][key2],test[key1][key3])



