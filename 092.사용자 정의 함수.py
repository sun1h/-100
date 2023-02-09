def makit(n):
    total=0
    for i in range(n+1):
        total+=i
    return total
makit(10)
makit(100)

print(f'1부터 10까지 합은 {makit(10)} 입니다.')
print(f'1부터 100까지 합은 {makit(100)} 입니다.')
