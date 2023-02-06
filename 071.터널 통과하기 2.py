car_h=int(input())
t1,t2,t3 = map(int, input().split())
li=[t1,t2,t3]
no=[]

for check in li:
    if check <= car_h:
        no.append(check)
    else:
        pass

no =list(map(str, no))

if no == []:
    print('터널 통과 가능')
else:
    print('터널 통과 불가능')
    for i in range(len(no)):
        print(no[i])