def makit(n1,n2): # 두 숫자를 입력받은 함수 
    x = makit_abs(n1) # 숫자 하나를 입력받아 절댓값을 보내주는 함수 makit_abs
    y = makit_abs(n2) # 두 번째 숫자 n2의 절댓값을 구해 y에 저장

    if x > y: # 두 숫자 n1,n2의 절댓값 x,y의 값 비교
        print(n1,n2,'절댓값이 큰 수는: ',n1)
    else:
        print(n1,n2,'절댓값이 큰 수는: ',n2)

def makit_abs(n):   # 숫자 하나를 입력받아 절댓값을 구하는 함수
    if n >=0:
        return n
    else:
        return -n

makit(11,-13)
makit(15,79)