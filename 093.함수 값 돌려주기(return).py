def makit(n1, n2):
    total=0
    for i in range(n1,n2+1):
        total+=i
    return total
    
n1 = int(input('첫 번째 숫자를 입력하세요'))
n2 = int(input('두 번째 숫자를 입력하세요'))

print(makit(n1,n2))