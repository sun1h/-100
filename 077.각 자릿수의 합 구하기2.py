#붙어있는 숫자열 떨어트리기
num=int(input())
li=[]
while num/10 > 0: #반복횟수를 알기 어려우니 무한루프 사용
    li.append(num%10)
    num=num//10

total=0
for x in li:
    total+=x

print(total)


#for문을 써야된다면
num=int(input())
st=str(num)
total=0
for i in range(len(st)):
    total+=(num%10)
    num=num//10

print(total)


#또 다른방법
N=input()
answer = 0
for n in str(N):
	answer+=int(n)

print(answer)


#한줄로 작성
print(sum(map(int, input())))