a = [13, 7, 2, 199, 24, 5]

def makit_selection(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] < a[j]:
                a[i],a[j] = a[j],a[i]
    return a


print('최종 정렬 결과', makit_selection(a))