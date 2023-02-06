num=int(input())
li=list(map(int,input().split()))
li.sort()

total=0
for x in li:
    total+=x

print(f'리스트 최댓값 {li[-1]}\n리스트 최솟값 {li[0]}\n리스트 평균값 {(total/num)}')