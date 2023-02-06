num=1000
li=[]
for i in range(1,num+1):  #입력값도 들어가야 하니깐 +1
    li.append(i)

str_li=list(map(str,li))
st=''.join(str_li) #한줄짜리 문자열로 만들어서 문자찾기
                   #int의 경우는 17을 1,7로 나누어서 생각못함

print(st.count('7'))