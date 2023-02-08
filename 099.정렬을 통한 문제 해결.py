name = ['메이킷', '소피아', '우진', '시은', '하워드'] # 학생 이름 리스트
score = [92, 75, 95, 96, 89] # 학생 점수 리스트

n = int(input('몇 등 학생 자료를 알고 싶나요? '))

li=[]
for pair in zip(score,name):
    li.append(pair)
li.sort(key=lambda x:x[0],reverse=True)

a=li[n-1][0]
name_1=li[n-1][1]
idx=name.index(name_1)
print(name[idx])

print(n, '등 학생은', a, '점이고 이름은', name[idx], '입니다') # 결과 출력