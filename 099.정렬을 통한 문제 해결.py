name = ['메이킷', '소피아', '우진', '시은', '하워드'] # 학생 이름 리스트
score = [92, 75, 95, 96, 89] # 학생 점수 리스트

n = int(input('몇 등 학생 자료를 알고 싶나요? '))

li=[]
for i in range(name):
    li.append(name[i],score[i])

print(li)
#print(n, '등 학생은', a, '점이고 이름은', name[idx], '입니다') # 결과 출력