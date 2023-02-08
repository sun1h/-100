left  = ['초록', '초록', '빨강', '노랑', '노랑', '파랑', '남색', '보라']
right = ['파랑', '초록', '초록', '보라', '보라', '노랑', '빨강', '빨강', '파랑']
def makit(left,right):
    color = ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']

    # num = [0]*len(color) 또는 num = [0 for i in range(7)]

    left_num = [0, 0, 0, 0, 0, 0, 0] # 무지개 색깔 순서대로 왼손 장갑 개수
    right_num = [0, 0, 0, 0, 0, 0, 0] # 무지가 색깔 순서대로 오른손 장갑 개수

    for i in range(len(color)):
        for j in range(len(left)):
            if color[i] == left[j]:
                left_num[i] += 1
        for j in range(len(right)):
            if color[i] == right[j]:
                right_num[i] += 1
    same=[]
    for i in range(7):
        if left_num[i] > right_num[i]:
            same.append(right_num[i])
        elif left_num[i] < right_num[i]:
            same.append(left_num[i])
        else:
            same.append(right_num[i])
        print(f'{color[i]} 색으로 만들 수 있는 장갑은 {same[i]} 개')
        #또는 min 내장함수 써도 됨
        
    total=0
    for s in same:
        total+=s
    #total=sum(same) 이렇게 내장함수 써도됨

    return total

print('최대로 만들 수 있는 장갑 쌍은', makit(left,right), '개')