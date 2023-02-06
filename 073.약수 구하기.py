num=int(input())
li=[]
for i in range(1,num+1):  #0으로 나누는거 제외시키기
    if int(num/i) == (num/i):
        li.append(int(num/i))

lis=sorted(li)
print(*lis, sep=' ') #숫자 리스트 괄호 없애기 (언패킹)
# lis2=sorted(li,reverse=True) #내림차순 -> 사실 for문 돌면서 이미 큰수부터 정렬된거라서 안해도 됨
# print(*lis2,sep=' ')
print(*li, sep=' ')