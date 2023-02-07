s = {'사는 곳':'인천 송도', '성별':'남자','이름':'우진'}
a=list(s.keys())
b=list(s.values())
c=list(s.items())
print(a)
print(b)
print(c)

#리스트 안해주면 아래처럼 출력됨
'''
dict_keys(['사는 곳', '성별', '이름'])
dict_values(['인천 송도', '남자', '우진'])
dict_items([('사는 곳', '인천 송도'), ('성별', '남자'), ('이름', '우진')])
'''