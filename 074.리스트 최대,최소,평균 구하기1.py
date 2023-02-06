num=int(input())
li=list(map(int,input().split()))
li.sort()

# max=li[-1]
# min=li[0]
# ave=sum(li)/num
#내장함수 없이 sum구하는법 ->75번
# num=0
# for x in li:
#     num+=x

print(f'리스트 최댓값 {li[-1]}\n리스트 최솟값 {li[0]}\n리스트 평균값 {(sum(li)/num)}')